from django.views.generic import CreateView, DetailView, ListView, View, UpdateView, DeleteView
from webapp.models import Poll, Choice
from django.urls import reverse_lazy
from webapp.forms import PollForm, ChoiceForm, SearchForm, PollDeleteForm
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.db.models import Q
from django.utils.http import urlencode


class PollIndexView(ListView):

    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ('question', 'created_at')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(PollIndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(question__icontains=self.search_data) |
                Q(created_at__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class PollCreateView(CreateView):

    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollChoiceCreate(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll_view', pk=poll.pk)


class PollView(DetailView):
    model = Poll
    template_name = 'poll/view.html'
    context_object_name = 'poll'


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):

    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('poll_list')



