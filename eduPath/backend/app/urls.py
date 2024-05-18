from django.urls import path
from .views import get_university_by_name, search_universities
from app import views
from django.contrib import messages


urlpatterns = [
     path('universities/<str:university_name>/', get_university_by_name, name='university_list_by_name'),
     path('search/', search_universities, name='search_universities'),
     path('accesToUniversities/', views.universities_view, name='universities'),
     path('', views.landing, name='landing'),
     path('contact/', views.contact_page, name='contact'),
     path('abts/', views.abts_page, name='about_us'),
     path('reg/', views.reg_page, name='reg'),
     path('login/', views.login_page, name='login'),
     path('landing/', views.landing, name='landing'),


]
