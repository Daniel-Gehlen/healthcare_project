from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.authentication, name='authentication'),
    path('appointment_schedule/', views.appointment_schedule, name='appointment_schedule'),
]
