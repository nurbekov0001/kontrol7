from django.contrib import admin

from django.contrib import admin
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['question']
    fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'poll']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
# Register your models here.

# Register your models here.
