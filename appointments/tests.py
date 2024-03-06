from django.test import TestCase
from django.contrib.auth.models import User
from .models import Appointment
from datetime import date, time


class AppointmentTestCase(TestCase):
    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')

        # Criar exemplos de consultas
        self.appointment1 = Appointment.objects.create(
            user=self.user,
            doctor='Dr. Smith',
            date=date(2024, 3, 5),
            time=time(10, 0)
        )

        self.appointment2 = Appointment.objects.create(
            user=self.user,
            doctor='Dr. Johnson',
            date=date(2024, 3, 6),
            time=time(11, 0)
        )

    def test_appointment_creation(self):
        """Teste para verificar se o agendamento foi criado corretamente."""
        self.assertEqual(self.appointment1.user, self.user)
        self.assertEqual(self.appointment1.doctor, 'Dr. Smith')
        self.assertEqual(self.appointment1.date, date(2024, 3, 5))
        self.assertEqual(self.appointment1.time, time(10, 0))

    def test_get_user_appointments(self):
        """Teste para verificar se as consultas de um usuário são recuperadas corretamente."""
        user_appointments = Appointment.objects.filter(user=self.user)
        self.assertEqual(user_appointments.count(), 2)
        self.assertIn(self.appointment1, user_appointments)
        self.assertIn(self.appointment2, user_appointments)

    def test_delete_appointment(self):
        """Teste para verificar se uma consulta é excluída corretamente."""
        appointment_count_before_delete = Appointment.objects.count()
        self.appointment1.delete()
        appointment_count_after_delete = Appointment.objects.count()
        self.assertEqual(appointment_count_after_delete, appointment_count_before_delete - 1)
