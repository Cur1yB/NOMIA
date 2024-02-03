# quiz/quiz_app/admin.py

from django.contrib import admin
from .models import UserResponse, Question, AnswerOption
# Register your models here.

from django.contrib import admin
from .models import UserResponse, Question, AnswerOption

# Определите классы ModelAdmin для настройки представления моделей в админ-панели

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'selected_option')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type')

class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')

# Регистрируйте модели и их ModelAdmin классы

admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerOption, AnswerOptionAdmin)
