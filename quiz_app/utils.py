# quiz/quiz_app/utils.py

from django.db import connection
from collections import OrderedDict

def get_total_participants(): 
    # Вычисляет общее количество уникальных участников опроса, основываясь на количестве уникальных сессий.
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(DISTINCT session_key) FROM quiz_app_userresponse")
        total_participants = cursor.fetchone()[0]
    return total_participants

def get_choice_statistics(request): 
    # Возвращает статистику по выборам ответов на вопросы для текущей сессии пользователя.
    last_test_question_ids = request.session.get('answered_questions', [])
    if not last_test_question_ids:
        return []

    question_ids_str = ','.join(map(str, last_test_question_ids))

    with connection.cursor() as cursor:
        # Запрос для получения статистики по каждому варианту ответа
        answers_statistics_query = f"""
        SELECT 
            qr.question_id,
            q.text AS question_text,
            aro.text AS option_text,
            COUNT(qr.id) AS option_count,
            COUNT(qr.id) * 100.0 / sub.total_responses AS option_rate,
            sub.total_responses
        FROM 
            quiz_app_userresponse qr
        INNER JOIN 
            quiz_app_answeroption aro ON qr.selected_option_id = aro.id
        INNER JOIN 
            quiz_app_question q ON qr.question_id = q.id
        INNER JOIN (
            SELECT 
                question_id, 
                COUNT(id) AS total_responses 
            FROM 
                quiz_app_userresponse 
            WHERE 
                question_id IN ({question_ids_str})
            GROUP BY 
                question_id
        ) sub ON qr.question_id = sub.question_id
        WHERE 
            qr.question_id IN ({question_ids_str})
        GROUP BY 
            qr.question_id, q.text, aro.text, sub.total_responses
        ORDER BY 
            qr.question_id, option_count DESC
        """
        cursor.execute(answers_statistics_query)
        answers_statistics = cursor.fetchall()
        statistics = []
        for answer_stat in answers_statistics:
            question_id, question_text, option_text, option_count, option_rate, total_responses = answer_stat
            print(f'Вопрос ID: {question_id}, Вопрос: {question_text}, Опция: {option_text}, Кол-во ответов: {option_count}, Доля: {option_rate:.2f}%, Общее количество ответов: {total_responses}')
            statistics.append({
                'question_id': question_id,
                'option_text': option_text,
                'option_count': option_count,
                'option_rate': option_rate,
                'question_text': question_text,
                'total_responses': total_responses,
            })

    return statistics
    
def get_text_answers_statistics(request): 
    # Собирает статистику по текстовым ответам пользователя в текущей сессии.
    last_test_question_ids = request.session.get('answered_questions', [])
    if not last_test_question_ids:
        return []

    question_ids_str = ','.join(map(str, last_test_question_ids))
    with connection.cursor() as cursor:
        text_answers_query = f"""
        SELECT 
            qr.question_id,
            q.text AS question_text,
            qr.answer_text,
            COUNT(qr.id) AS answer_count,
            COUNT(qr.id) * 100.0 / total_responses.total AS answer_rate,
            total_responses.total AS total_responses
        FROM 
            quiz_app_userresponse qr
        INNER JOIN quiz_app_question q ON qr.question_id = q.id
        INNER JOIN (
            SELECT 
                question_id, 
                COUNT(id) AS total
            FROM 
                quiz_app_userresponse
            WHERE 
                question_id IN ({question_ids_str}) AND
                answer_text IS NOT NULL
            GROUP BY 
                question_id
        ) AS total_responses ON qr.question_id = total_responses.question_id
        WHERE 
            qr.question_id IN ({question_ids_str}) AND
            qr.answer_text IS NOT NULL
        GROUP BY 
            qr.question_id, q.text, qr.answer_text, total_responses.total
        ORDER BY 
            qr.question_id, answer_count DESC
        """
        cursor.execute(text_answers_query)
        text_answers_statistics = cursor.fetchall()

        statistics = []
        for stat in text_answers_statistics:
            question_id, question_text, answer_text, answer_count, answer_rate, total_responses = stat
            statistics.append({
                'question_id': question_id,
                'question_text': question_text,
                'answer_text': answer_text,
                'answer_count': answer_count,
                'answer_rate': answer_rate,
                'total_responses': total_responses
            })

    return statistics
  
def transform_statistics(choice_statistics, text_statistics):
    # Объединяет статистику по выборам и текстовым ответам, подготавливая данные для вывода.
    questions_dict = OrderedDict()
    merged_statistics = []
    for stat in choice_statistics:
        merged_statistics.append(stat)
    for stat in text_statistics:
        if 'total_responses' not in stat:
            stat['total_responses'] = calculate_total_responses_for_text(stat['question_id'], choice_statistics)
        merged_statistics.append(stat)

    # Обработка объединенной статистики
    for stat in merged_statistics:
        question_id = stat['question_id']
        if question_id not in questions_dict:
            questions_dict[question_id] = {
                'question_text': stat['question_text'],
                'options': [],
                'total_responses': stat['total_responses'],
                'rank': 0
            }

        option_or_answer_text = stat.get('option_text', 'Текстовый ответ: ' + stat.get('answer_text', ''))
        count = stat.get('option_count', stat.get('answer_count', 0))
        rate = stat.get('option_rate', stat.get('answer_rate', 0.0))
        
        # Добавление статистики варианта ответа или текстового ответа
        questions_dict[question_id]['options'].append({
            'text': option_or_answer_text,
            'count': count,
            'rate': rate
        })

    # Рассчитываем ранги после объединения всех статистических данных
    calculate_question_ranks(questions_dict)

    return list(questions_dict.values())

def calculate_total_responses_for_text(question_id, choice_statistics):
    # Рассчитывает общее количество ответов на текстовые вопросы для поддержки статистики.
    return sum(stat['total_responses'] for stat in choice_statistics if stat['question_id'] == question_id)

def calculate_question_ranks(questions_dict):
    # Ранжирует вопросы в зависимости от общего количества ответов, поддерживая порядковые номера для вопросов 
    # с одинаковым количеством ответов.
    current_rank = 1
    last_total_responses = None
    for question in questions_dict.values():
        if last_total_responses is not None and question['total_responses'] != last_total_responses:
            current_rank += 1
        question['rank'] = current_rank
        last_total_responses = question['total_responses']

def get_all_questions_choice_statistics():
    # Генерирует статистику по всем вариантам ответов в базе данных, независимо от сессии пользователя.
    with connection.cursor() as cursor:
        # Запрос для получения статистики по каждому варианту ответа для всех вопросов
        answers_statistics_query = """
        SELECT 
            qr.question_id,
            q.text AS question_text,
            aro.text AS option_text,
            COUNT(qr.id) AS option_count,
            COUNT(qr.id) * 100.0 / sub.total_responses AS option_rate,
            sub.total_responses
        FROM 
            quiz_app_userresponse qr
        INNER JOIN 
            quiz_app_answeroption aro ON qr.selected_option_id = aro.id
        INNER JOIN 
            quiz_app_question q ON qr.question_id = q.id
        INNER JOIN (
            SELECT 
                question_id, 
                COUNT(id) AS total_responses 
            FROM 
                quiz_app_userresponse 
            GROUP BY 
                question_id
        ) sub ON qr.question_id = sub.question_id
        GROUP BY 
            qr.question_id, q.text, aro.text, sub.total_responses
        ORDER BY 
            qr.question_id, option_count DESC
        """
        cursor.execute(answers_statistics_query)
        rows = cursor.fetchall()

        # Преобразование кортежей в список словарей
        statistics = [
            {
                'question_id': row[0],
                'question_text': row[1],
                'option_text': row[2],
                'option_count': row[3],
                'option_rate': row[4],
                'total_responses': row[5],
            }
            for row in rows
        ]

    return statistics
    
def get_all_questions_text_answers_statistics():
    # Собирает статистику по всем текстовым ответам в базе данных.
    with connection.cursor() as cursor:
        # Запрос для получения статистики по текстовым ответам для всех вопросов
        text_answers_query = """
        SELECT 
            qr.question_id,
            q.text AS question_text,
            qr.answer_text,
            COUNT(qr.id) AS answer_count,
            COUNT(qr.id) * 100.0 / total_responses.total AS answer_rate,
            total_responses.total AS total_responses
        FROM 
            quiz_app_userresponse qr
        INNER JOIN quiz_app_question q ON qr.question_id = q.id
        INNER JOIN (
            SELECT 
                question_id, 
                COUNT(id) AS total
            FROM 
                quiz_app_userresponse
            WHERE 
                answer_text IS NOT NULL
            GROUP BY 
                question_id
        ) AS total_responses ON qr.question_id = total_responses.question_id
        WHERE 
            qr.answer_text IS NOT NULL
        GROUP BY 
            qr.question_id, q.text, qr.answer_text, total_responses.total
        ORDER BY 
            qr.question_id, answer_count DESC
        """
        cursor.execute(text_answers_query)
        rows = cursor.fetchall()

        # Преобразование кортежей в список словарей
        statistics = [
            {
                'question_id': row[0],
                'question_text': row[1],
                'answer_text': row[2],
                'answer_count': row[3],
                'answer_rate': row[4],
                'total_responses': row[5],
            }
            for row in rows
        ]

    return statistics