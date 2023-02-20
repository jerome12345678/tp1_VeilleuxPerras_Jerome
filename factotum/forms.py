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


class SearchProfessionnal(forms.Form):
    SERVICES = (
        ('Charpentier', '1'),
        ('Électricien', '2'),
        ('Plombier', '3'),
        ('EntretienMénager', '4'),
        ('EntretienPaysager', '5'),
    )
    services = forms.ChoiceField(choices=SERVICES)
    code_postal = forms.CharField(min_length=6, max_length=6, required=True)


class AjoutServiceProfessionnel(forms.Form):
    SERVICES = (
        ('Charpentier', '1'),
        ('Électricien', '2'),
        ('Plombier', '3'),
        ('EntretienMénager', '4'),
        ('EntretienPaysager', '5'),
    )
    field = forms.ChoiceField(choices=SERVICES)
    taux_horaire = forms.IntegerField(required=True)


