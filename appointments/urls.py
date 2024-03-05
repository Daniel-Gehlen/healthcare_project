# appointments/urls.py

from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial do aplicativo de agendamento
    # Adicione outras URLs conforme necessário para suas visualizações
]
