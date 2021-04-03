from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        db_table = 'Polls'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return f'{self.id}. {self.question}:{self.created_at}'


class Choice(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Вариант ответа")
    poll = models.ForeignKey("webapp.Poll", related_name='poll', on_delete=models.CASCADE,
                             verbose_name="Опрос")

    def __str__(self):
        return f'{self.id}. {self.text}:{self.poll}'


class Answer (models.Model):
    poll_poll = models.ForeignKey("webapp.Poll", related_name='poll_poll', on_delete=models.CASCADE,
                             verbose_name="Опрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    possible_answer = models.ForeignKey("webapp.Choice", related_name='poll_answer', on_delete=models.CASCADE,
                             verbose_name="Вариант ответа")

    def __str__(self):
        return f'{self.id}. {self.poll_poll}:{self.created_at}.{self.possible_answer}'