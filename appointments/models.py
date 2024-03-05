# models.py

from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que fez o agendamento
    doctor = models.CharField(max_length=100)  # Nome do médico
    date = models.DateField()  # Data da consulta
    time = models.TimeField()  # Horário da consulta
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do agendamento

    def __str__(self):
        return f"Appointment {self.pk} - {self.doctor} - {self.date} {self.time}"
