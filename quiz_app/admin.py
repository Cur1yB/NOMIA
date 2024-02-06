# quiz/quiz_app/admin.py

from django.contrib import admin
from .models import UserResponse, Question, AnswerOption

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'selected_option', 'session_key', 'is_correct')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type')

class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerOption, AnswerOptionAdmin)
