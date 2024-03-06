from datetime import datetime

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponseServerError
from django.shortcuts import render, redirect

from .forms import SignUpForm, AppointmentForm
from .models import Appointment, HealthProfessional


def appointment_history(request):
    try:
        # Obtenha todas as consultas do banco de dados
        appointments = Appointment.objects.all()

        # Renderize o template com os dados das consultas no contexto
        return render(request, 'appointment_history.html', {'appointments': appointments})
    except Exception as e:
        # Se ocorrer um erro, imprima o erro no console para fins de depuração
        print(f"Erro ao renderizar a página de histórico de consultas: {e}")
        # Retorne uma resposta HTTP com um status de erro 500 (Internal Server Error)
        return HttpResponseServerError("Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde.")


def appointment_scheduler(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_history')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_scheduler.html', {'form': form})


def get_available_times(request):
    selected_date = request.GET.get('appointment_date')
    health_professional_id = request.GET.get('health_professional')
    available_times = fetch_available_times_from_legacy_system(selected_date, health_professional_id)
    return JsonResponse(available_times, safe=False)


def fetch_available_times_from_legacy_system(selected_date, health_professional_id):
    try:
        response = requests.get(
            f'https://sistema-legado.com/api/appointments/{selected_date}/{health_professional_id}/times')
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.RequestException as e:
        print(
            f"Erro ao obter horários disponíveis para a data {selected_date} e profissional {health_professional_id}: {e}")
        return ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00']


def schedule_appointment(request):
    if request.method == 'POST':
        user = request.user
        health_professional_id = request.POST.get('health_professional')
        date = request.POST.get('appointment_date')
        time = request.POST.get('time')

        health_professional = HealthProfessional.objects.get(id=health_professional_id)

        # Criar o objeto de consulta agendada
        Appointment.objects.create(user=user, health_professional=health_professional, date=date,
                                   time=time)

        # Redirecionar para a página de histórico de consultas
        appointments = Appointment.objects.filter(user=user)
        return render(request, 'appointment_history.html', {'appointments': appointments})

    # Se não for uma solicitação POST, renderizar a página de agendamento com os horários disponíveis
    professionals = HealthProfessional.objects.all()
    selected_date = request.GET.get('appointment_date')
    available_times = get_available_times(selected_date)
    return render(request, 'appointment_schedule.html',
                  {'professionals': professionals, 'available_times': available_times})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    'user_profile')  # Redireciona para a página do perfil do usuário após o login bem-sucedido
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')  # Redireciona para a página inicial após o cadastro bem-sucedido
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view():
    # Your logout logic here
    return redirect('base')


def user_profile(request):
    # Lógica para renderizar a página do perfil do usuário
    return render(request, 'user_profile.html')


def base_page(request):
    return render(request, 'base.html')
