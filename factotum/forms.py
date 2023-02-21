from django import forms

from tp1_VeilleuxPerras_Jerome import settings
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
        (1, 'Charpentier'),
        (2, 'Électricien'),
        (3, 'Plombier'),
        (4, 'EntretienMénager'),
        (5, 'EntretienPaysager'),
    )
    services = forms.IntegerField()
    code_postal = forms.CharField(min_length=6, max_length=6, required=True)


class AjoutServiceProfessionnel(forms.Form):
    SERVICES = (
        (1, 'Charpentier'),
        (2, 'Électricien'),
        (3, 'Plombier'),
        (4, 'EntretienMénager'),
        (5, 'EntretienPaysager'),
    )
    services = forms.IntegerField()
    taux_horaire = forms.IntegerField(required=True)


class AjoutSoumission(forms.Form):
    date_planification = forms.DateField()
    description = forms.CharField(widget=forms.Textarea, required=True)



