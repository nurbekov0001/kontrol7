from django import forms
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)


class PollDeleteForm(forms.Form):
    question = forms.CharField(max_length=100, required=True, label='Введите название вопроса, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)


class ChoiceDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название Ответа, чтобы удалить её')




