# quiz/quiz_app/models.py

from django.db import models

class Question(models.Model):
    TEXT = 'T'
    CHOICE = 'C'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (CHOICE, 'Choice'),
    ]
    
    text = models.CharField(max_length=1024, unique=True)
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES, default=TEXT)
    DIFFICULTY_LEVELS = [(i, str(i)) for i in range(1, 6)]
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS, default=1)

    def __str__(self):
        return self.text


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)  # Для текстовых ответов
    selected_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE, null=True, blank=True)  # Для ответов с выбором
    is_correct = models.BooleanField(default=False)  
    session_key = models.CharField(max_length=40, default='default_session_key')

    def __str__(self):
        return f"Response to {self.question.text} by {self.id}"
