from django.db import models
from django.contrib.auth.models import User


class HealthProfessional(models.Model):
    objects = None
    name = models.CharField(max_length=100)  # Nome do profissional de saúde

    def __str__(self):
        return self.name


class Appointment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que fez o agendamento
    health_professional = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE)  # Profissional de saúde da consulta
    date = models.DateField()  # Data da consulta
    time = models.TimeField()  # Horário da consulta
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do agendamento

    def __str__(self):
        return f"Appointment {self.pk} - {self.health_professional} - {self.date} {self.time}"
