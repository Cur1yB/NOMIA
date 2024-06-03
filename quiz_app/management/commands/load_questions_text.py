# quiz/quiz_app/management/commands/load_questions_text.py

from django.core.management.base import BaseCommand
from quiz_app.models import Question, AnswerOption
from .questions_ import text_questions_and_answers

class Command(BaseCommand):
    help = 'Load a list of text questions and answers into the database'

    def handle(self, *args, **kwargs):
        for question_text, data in text_questions_and_answers.items():
            # Извлекаем текст ответа и сложность из кортежа
            answer_text, difficulty = data
            # Создаем вопрос с указанными значениями
            question, created = Question.objects.get_or_create(
                text=question_text,
                defaults={'question_type': Question.TEXT, 'difficulty': difficulty}
            )
            if created:
                # Если вопрос создан, добавляем вариант ответа
                AnswerOption.objects.create(
                    question=question,
                    text=answer_text,
                    is_correct=True  # Поскольку это текстовый ответ, предполагаем его правильность
                )
            else:
                self.stdout.write(self.style.WARNING(f'Question "{question_text}" already exists. Skipped.'))
        self.stdout.write(self.style.SUCCESS('Successfully loaded all text questions and answers.'))
