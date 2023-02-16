from distutils.command import upload

from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import User, Soumission
from django.contrib import messages


# Create your views here.
def index (request):
    return render(request, 'factotum/base.html')

def profil(request):
    soumissions = Soumission.objects.all()
    return render(request, 'factotum/profil_details.html', {'soumissisons': soumissions})


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.data['email'] != "":
            adresse = User.objects.filter(email=form.data['email'])

            if len(adresse) != 0:
                messages.add_message(request, messages.INFO, 'Cette adresse est déjà utilisé')

        if form.is_valid() and request.FILES['avatar']:
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

