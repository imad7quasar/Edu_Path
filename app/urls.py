from django.urls import path
from .views import get_university_by_name

urlpatterns = [
     path('universities/<str:university_name>/', get_university_by_name, name='university_list_by_name'),
]
