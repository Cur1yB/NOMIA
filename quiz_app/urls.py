# quiz/quiz_app/urls.py

from django.urls import path
from .views import question_view, start_page, end_of_quiz, view_statistics, view_all_questions_statistics

urlpatterns = [
    path('', start_page, name='start_page'),
    path('question/<int:question_id>/', question_view, name='question_view'),
    path('end_of_quiz/', end_of_quiz, name='end_of_quiz'),
    path('statistics/', view_statistics, name='view_statistics'),
    path('full_statistics/', view_all_questions_statistics, name='view_all_questions_statistics'),
]
