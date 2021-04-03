from django.urls import path
from webapp.views import (
    PollIndexView,
    PollDeleteView,
    PollChoiceCreate,
    PollCreateView,
    PollUpdateView,
    PollView,
    ChoiceView,
    ChoiceUpdateView,
    CoiceDeleteView

)

urlpatterns = [
    path('', PollIndexView.as_view(), name='poll_list'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),

    path('poll/add/', PollCreateView.as_view(), name='poll_add'),
    path('poll_choice/<int:pk>/add/', PollChoiceCreate.as_view(), name='poll_choice_add'),


    path('<int:pk>/', ChoiceView.as_view(), name='view'),
    path('<int:pk>/update/', ChoiceUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CoiceDeleteView.as_view(), name='delete'),



]
