from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário
    objects = models.Manager()


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário
    objects = models.Manager()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    # Adicione outros campos conforme necessário
    objects = models.Manager()
