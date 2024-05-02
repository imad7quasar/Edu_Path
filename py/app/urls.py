from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('submit/', views.submit_quiz_view, name='submit_quiz'),  # URL pattern for submitting the quiz form
    path('thank-you/', views.thank_you_view, name='thank_you'),
]
