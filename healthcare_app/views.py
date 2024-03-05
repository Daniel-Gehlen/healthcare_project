from django.shortcuts import render
from .models import Patient


def home(request):
    patients = Patient.objects.all()
    return render(request, 'home.html', {'patients': patients})


def authentication(request):
    # Sua lógica de autenticação aqui
    return render(request, 'authentication.html')


def appointment_schedule(request):
    # Sua lógica de agendamento de consulta aqui
    return render(request, 'appointment_calendar.html')
