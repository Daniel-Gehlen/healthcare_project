from django.contrib import admin
from .models import Patient, Appointment, Doctor

# Registrar os modelos para aparecerem no painel de administração
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor)
