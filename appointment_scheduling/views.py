# appointment_scheduling/views.py
from django.shortcuts import render, get_object_or_404
from .models import Appointment


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_scheduling/appointment_list.html', {'appointments': appointments})


def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment_scheduling/appointment_detail.html', {'appointment': appointment})
