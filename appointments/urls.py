from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', views.base_page, name='base'),
    path('base/', views.base_page, name='base'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('scheduler/', views.appointment_scheduler, name='appointment_scheduler'),

    path('history/', views.appointment_history, name='appointment_history'),
    # Adicione outras URLs conforme necessário
]
