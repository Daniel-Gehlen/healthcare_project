# appointment_scheduling/utils.py
from .models import Appointment


def check_availability(appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        return appointment.available  # Supondo que há um campo 'available' no modelo Appointment
    except Appointment.DoesNotExist:
        return False


def update_appointment_status(appointment_id, status):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = status
        appointment.save()
        return True
    except Appointment.DoesNotExist:
        return False
