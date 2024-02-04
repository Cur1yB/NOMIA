# quiz/quiz_app/forms.py

from django import forms
from .models import UserResponse, AnswerOption

class TextForm(forms.ModelForm):
    answer_text = forms.CharField(label='Ваш ответ', widget=forms.TextInput(attrs={'placeholder': 'Введите ваш ответ здесь'}))

    class Meta:
        model = UserResponse
        fields = ['answer_text']

class ChoiceForm(forms.ModelForm):
    selected_option = forms.ModelChoiceField(queryset=AnswerOption.objects.none(), widget=forms.RadioSelect, empty_label=None)

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id', None)
        super(ChoiceForm, self).__init__(*args, **kwargs)
        if question_id:
            # Загружаем варианты ответов в случайном порядке
            self.fields['selected_option'].queryset = AnswerOption.objects.filter(question_id=question_id).order_by('?')


    class Meta:
        model = UserResponse
        fields = ['selected_option']
