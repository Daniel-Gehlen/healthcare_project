from django.shortcuts import render
from .models import Appointment


def index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/index.html', {'appointments': appointments})
