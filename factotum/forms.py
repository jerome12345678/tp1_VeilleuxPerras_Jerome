from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "code_Postal", "email", "password1",
                  "password2", "role", "avatar"]
        labels = {"username": "pseudo"}, {"password1": "mot de passe"}, \
            {"password2": "confirmation du mot de passe"}
