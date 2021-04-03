from django.views.generic import View
from webapp.models import Answer, Poll, Choice
from django.shortcuts import get_object_or_404, redirect, reverse, render

class AnswerCreate(View):

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        answers = poll.poll.all()

        pk = kwargs.get("pk")
        return render(request, 'collecting_answers/create.html', {"pk": pk, 'answers': answers, "poll": poll})

    def post (self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        print(request.POST)
        choice = get_object_or_404(Choice, pk=request.POST['answer'])

        answer = Answer.objects.create(
            poll_poll=poll,
            possible_answer=choice,
        )

        return redirect('poll_view', pk=kwargs.get('pk'))

