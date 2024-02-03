# quiz/quiz_app/urls.py

from django.urls import path
from .views import question_view

urlpatterns = [
    path('question/<int:question_id>/', question_view, name='question_view'),
]