# quiz/quiz_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from quiz_app.forms import ChoiceForm, TextForm, AnswerOption, UserResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import (get_choice_statistics, transform_statistics, get_text_answers_statistics, 
                    get_all_questions_choice_statistics, get_all_questions_text_answers_statistics,
                    get_total_participants)

def start_page(request):
    first_question_id = Question.objects.order_by('id').first().id
    request.session.clear()
    return render(request, 'start_page.html', {'first_question_id': first_question_id})

def end_of_quiz(request):
    score = calculate_quiz_results(request)
    return render(request, 'end_of_quiz.html', {'score': score})

def question_view(request, question_id):
    # Получаем текущий вопрос из таблицы с вопросами 
    question = get_object_or_404(Question, id=question_id) 
    # Инициализация формы
    if question.question_type == Question.TEXT:
        form = TextForm(request.POST or None)
    else:
        form = ChoiceForm(request.POST or None, question_id=question.id)
    
    # Инициализация или обновление счетчика вопросов в сессии
    questions_answered = request.session.get('questions_answered', 0) + 1
    if questions_answered >= 11:
        return HttpResponseRedirect(reverse('end_of_quiz'))

    if request.method == 'POST' and form.is_valid():
        # Сохраняем ответ пользователя
        user_response = form.save(commit=False)
        user_response.question = question
        if not request.session.session_key:
            request.session.create()
        user_response.session_key = request.session.session_key
        
        # Проверяем правильность ответа
        is_correct = check_answer_correctness(question, form)
        if is_correct:
            user_response.is_correct = True # по умолчанию False
        user_response.save()

        # Обновляем данные в сессии
        update_session_data(request, question.id, user_response.id) 
        
        # Определяем следующий вопрос
        next_question = determine_next_question(request, is_correct)
        return redirect('question_view', question_id=next_question.id)
    
    return render(request, 'quiz_template.html', {
        'form': form, 
        'question': question,
        'current_question_number': questions_answered
    })

def check_answer_correctness(question, form): 
    # Проверяем, правильно ли пользователь ответил на вопрос
    if question.question_type == Question.CHOICE:
        return form.cleaned_data['selected_option'].is_correct
    correct_answer = AnswerOption.objects.filter(question=question, is_correct=True).first()
    return form.cleaned_data['answer_text'].strip().lower() == correct_answer.text.strip().lower()

def update_session_data(request, question_id, user_response_id):
    questions_answered = request.session.get('questions_answered', 0) + 1 
    request.session['questions_answered'] = questions_answered # Обновляем номер текущего вопроса (порядковый, от 1 до 10)
    answered_questions = request.session.get('answered_questions', [])
    answered_questions.append(question_id) # добавляем id того вопроса, на который мы ответили из таблицы вопросов
    # Создаем или обновляем список идентификаторов ответов пользователя в сессии
    user_responses_ids = request.session.get('user_responses_ids', [])
    user_responses_ids.append(user_response_id) # добавляем id того вопроса, на который мы ответили из таблицы ответов пользователей
    request.session['answered_questions'] = answered_questions    
    request.session['user_responses_ids'] = user_responses_ids
   
def determine_next_question(request, is_correct): 
    # Функция определяющая, какой сложности будет следующий вопрос
    current_difficulty = request.session.get('current_difficulty', 1)
    answered_questions = request.session.get('answered_questions', [])
    available_questions = Question.objects.exclude(id__in=answered_questions)

    # Проверяем, есть ли доступные вопросы на текущем уровне сложности
    if not available_questions.filter(difficulty=current_difficulty).exists():
        # Если вопросы текущего уровня сложности закончились, увеличиваем сложность
        # независимо от того, был ответ верным или нет
        current_difficulty = min(current_difficulty + 1, 5)
    elif is_correct:
        # Если ответ был верным, увеличиваем сложность
        current_difficulty = min(current_difficulty + 1, 5)
    # В противном случае оставляем текущий уровень сложности без изменений

    request.session['current_difficulty'] = current_difficulty
    available_questions = Question.objects.exclude(id__in=answered_questions).filter(difficulty=current_difficulty)

    # Если после увеличения сложности вопросы все еще не доступны, пытаемся снизить сложность
    if not available_questions.exists() and current_difficulty > 1:
        current_difficulty -= 1
        available_questions = Question.objects.exclude(id__in=answered_questions).filter(difficulty=current_difficulty)

    request.session['current_difficulty'] = current_difficulty
    next_question = available_questions.order_by('?').first()

    if next_question:
        return next_question
    else:
        # Если вопросов больше нет, возвращаем None
        return None

def calculate_quiz_results(request):
    # Получаем все ответы пользователя из текущей сессии
    user_responses_ids = request.session.get('user_responses_ids', [])
    user_responses = UserResponse.objects.filter(id__in=user_responses_ids)
    score = 0
    # Проходим по каждому ответу пользователя
    for response in user_responses:
        print('response.is_correct', response.is_correct)
        if response.is_correct:
            # Увеличиваем счет на значение сложности вопроса
            score += response.question.difficulty
    # Возвращаем итоговый счет
    return score

def view_statistics(request): # Просмотр статистики в вопросах текущего опроса
    choice_statistics = get_choice_statistics(request)
    text_statistics = get_text_answers_statistics(request)
    statistics = transform_statistics(choice_statistics, text_statistics)
    total_participants = get_total_participants()
    context = {
        'statistics': statistics,
        'total_participants': total_participants 
    }
    return render(request, 'statistics.html', context)

def view_all_questions_statistics(request): # Просмотр статистики во всех вопросах
    choice_statistics = get_all_questions_choice_statistics()
    text_statistics = get_all_questions_text_answers_statistics()
    statistics = transform_statistics(choice_statistics, text_statistics)
    total_participants = get_total_participants()
    print(total_participants)
    context = {
        'statistics': statistics,
        'total_participants': total_participants 
    }
    return render(request, 'full_statistics.html', context)