from django.test import TestCase
from .models import Patient, Doctor, Appointment
from datetime import datetime


class ModelTestCase(TestCase):
    def setUp(self):
        # Criação de instâncias de pacientes, médicos e consultas para testar
        self.patient = Patient.objects.create(name="John Doe")
        self.doctor = Doctor.objects.create(name="Dr. Smith")
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_datetime=datetime.now()
        )

    def test_patient_creation(self):
        # Verifica se o paciente foi criado corretamente
        self.assertEqual(self.patient.name, "John Doe")

    def test_doctor_creation(self):
        # Verifica se o médico foi criado corretamente
        self.assertEqual(self.doctor.name, "Dr. Smith")

    def test_appointment_creation(self):
        # Verifica se a consulta foi criada corretamente
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.doctor, self.doctor)
        # Certifique-se de que o horário da consulta é uma instância de datetime
        self.assertIsInstance(self.appointment.appointment_datetime, datetime)
