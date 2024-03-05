# authentication/forms.py
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
