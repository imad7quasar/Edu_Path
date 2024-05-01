from django.urls import path
from .views import get_university_by_name, search_universities
from app import views

urlpatterns = [
     path('universities/<str:university_name>/', get_university_by_name, name='university_list_by_name'),
      path('search/', search_universities, name='search_universities'),
          path('accesToUniversities/', views.universities_view, name='universities'),
]
