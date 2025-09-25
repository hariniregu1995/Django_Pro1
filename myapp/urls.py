from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_course, name='add_course'),
    path('view/', views.view_courses, name='view_courses'),
]
