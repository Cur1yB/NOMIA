# quiz/quiz_app/urls.py

from django.urls import path
from .views import question_view, start_page, end_of_quiz

urlpatterns = [
    path('', start_page, name='start_page'),
    path('question/<int:question_id>/', question_view, name='question_view'),
    path('end_of_quiz/', end_of_quiz, name='end_of_quiz'),
]