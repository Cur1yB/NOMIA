# quiz/quiz_app/management/commands/load_questions_choices.py

from django.core.management.base import BaseCommand
from quiz_app.models import Question, AnswerOption
from .questions_ import questions_and_answers 

class Command(BaseCommand):
    help = 'Load a list of choice questions and answers into the database'

    def handle(self, *args, **kwargs):
        for question_text, data in questions_and_answers.items():
            answers, difficulty = data
            # Проверяем, существует ли уже такой вопрос
            question, created = Question.objects.get_or_create(
                text=question_text,
                defaults={'question_type': Question.CHOICE, 'difficulty': difficulty}
            )
            if created:
                # Если вопрос был создан, добавляем варианты ответов
                for i, answer_text in enumerate(answers):
                    AnswerOption.objects.create(
                        question=question,
                        text=answer_text,
                        is_correct=(i == 0)  # Предполагаем, что первый ответ всегда правильный
                    )
            else:
                self.stdout.write(self.style.WARNING(f'Question "{question_text}" already exists. Skipped.'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded all choice questions and answers.'))
