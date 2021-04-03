from django.views.generic import View
from webapp.models import Answer, Poll
from django.shortcuts import get_object_or_404, redirect, reverse, render

class AnswerCreate(View):

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        answers = poll.poll.all()

        pk = kwargs.get("pk")
        return render(request, 'collecting_answers/create.html', {"pk": pk, 'answers': answers, "poll": poll})

    def post (self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs.get('pk'))
        choice = get_object_or_404(Answer,)
        answer = Answer.objects.create(
            poll_poll=poll,
            possible_answer=
        )

        return redirect('poll_view', pk=kwargs.id)

