# quiz/quiz_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import ChoiceForm, TextForm

def question_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if question.question_type == Question.TEXT:
        form_class = TextForm
    else:
        form_class = ChoiceForm
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.question = question
            response.save()
            return redirect('next_question')
    else:
        form = form_class()
    
    return render(request, 'quiz_template.html', {'form': form, 'question': question})

'''# Импортируем необходимые функции и классы из Django и из текущего приложения
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import ChoiceForm, TextForm

# Определяем функцию представления для отображения вопросов
def question_view(request, question_id):
    # Используем функцию get_object_or_404 для получения объекта вопроса по его ID или возвращаем 404 ошибку, если объект не найден
    question = get_object_or_404(Question, id=question_id)
    
    # Проверяем тип вопроса. Если тип вопроса - текстовый (TEXT), то используем форму TextForm
    if question.question_type == Question.TEXT:
        form_class = TextForm
    # В противном случае (если вопрос с выбором), используем форму ChoiceForm
    else:
        form_class = ChoiceForm
    
    # Проверяем, был ли запрос отправлен методом POST (обычно это означает отправку формы)
    if request.method == 'POST':
        # Создаем экземпляр формы с данными из запроса
        form = form_class(request.POST)
        
        # Проверяем, валидны ли данные формы
        if form.is_valid():
            # Сохраняем форму с флагом commit=False, чтобы получить объект ответа без сохранения в базу данных
            response = form.save(commit=False)
            
            # Присваиваем вопрос объекту ответа, чтобы установить связь между ответом и вопросом
            response.question = question
            
            # Сохраняем объект ответа в базу данных
            response.save()
            
            # Перенаправляем пользователя на следующий вопрос или на другую страницу
            return redirect('next_question')
    # Если метод запроса не POST, то просто создаем пустую форму
    else:
        form = form_class()
    
    # Отрисовываем шаблон 'quiz_template.html', передавая ему форму и текущий вопрос
    return render(request, 'quiz_template.html', {'form': form, 'question': question})
'''