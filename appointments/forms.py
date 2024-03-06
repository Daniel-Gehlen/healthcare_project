from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from appointments.models import Appointment, HealthProfessional


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datepicker'}))

    class Meta:
        model = Appointment
        fields = ['health_professional', 'appointment_date']  # Corrija o nome do campo para 'health_professional'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            'health_professional'].queryset = HealthProfessional.objects.all()  # Ajuste para 'health_professional'
