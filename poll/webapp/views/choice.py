from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Choice
from django.views.generic import DetailView, UpdateView, DeleteView
from webapp.forms import ChoiceForm


class ChoiceView(DetailView):
    model = Choice
    template_name = 'choice/view.html'


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})



class CoiceDeleteView(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})





