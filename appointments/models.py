from django.db import models
from django.contrib.auth.models import User


class HealthProfessional(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    health_professional = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.pk} - {self.health_professional} - {self.date} {self.time}"
