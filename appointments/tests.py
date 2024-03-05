# tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Appointment
from datetime import date, time


class AppointmentTestCase(TestCase):
    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')

        # Criar um exemplo de consulta
        self.appointment = Appointment.objects.create(
            user=self.user,
            doctor='Dr. Smith',
            date=date(2024, 3, 5),
            time=time(10, 0)
        )

    def test_appointment_creation(self):
        """Teste para verificar se o agendamento foi criado corretamente."""
        self.assertEqual(self.appointment.user, self.user)
        self.assertEqual(self.appointment.doctor, 'Dr. Smith')
        self.assertEqual(self.appointment.date, date(2024, 3, 5))
        self.assertEqual(self.appointment.time, time(10, 0))
