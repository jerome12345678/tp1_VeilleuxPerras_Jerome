from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1",
                  "password2", "telephone", "code_Postal", "email", "adresse", "role", "avatar"]
        labels = {"username": "pseudo"}, {"password1": "mot de passe"}, \
            {"password2": "confirmation du mot de passe"}, {"first_name": "prénom"}, \
            {"last_name": "nom"}
