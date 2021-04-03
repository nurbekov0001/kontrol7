from django.contrib import admin

from django.contrib import admin
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['question']
    fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'poll']

class AnswerAdmin(admin.ModelAdmin):

    list_display = ['id', 'poll_poll', 'created_at','possible_answer']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)

# Register your models here.

# Register your models here.
