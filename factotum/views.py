from distutils.command import upload

from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import RegisterForm, SearchProfessionnal, AjoutServiceProfessionnel
from .models import User, Soumission, ProfessionnelService, Service
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'factotum/base.html')


def profil(request):
    soumissions = Soumission.objects.all()
    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissisons': soumissions, 'user_services': services})


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


def recherche(request):
    return render(request, "factotum/recherche.html")


def liste_professionnel(request):
    servicesPro = ProfessionnelService.objects.all()
    professionnels = []

    if request.method == "POST":
        form = SearchProfessionnal(data=request.POST)

        service = request.POST['services']
        code_postal = request.POST['code_postal']
        print(code_postal)

        for servicePro in servicesPro:
            if servicePro.service_id.nom == service:
                professionnels.append(servicePro)

        return render(request, 'factotum/professionnel_list.html', {'professionnels': professionnels})

    else:
        form = SearchProfessionnal()

    return render(request, 'factotum/professionnel_list.html', {'form': form})


def ajout_service(request, user_id):
    if request.method == "POST":
        form = AjoutServiceProfessionnel(data=request.POST)

        if form.is_valid():
            a = request.POST['services']
            taux_horaire = request.POST['taux_horaire']

            service = Service.objects.get(id=int(a))
            user = User.objects.get(id=request.user.id)

            ProfessionnelService.objects.create(taux_horaire=taux_horaire, service_id_id=service.id,
                                                utilisateur_id=user)

            services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)
            return render(request, 'factotum/profil_details.html', {'user_services': services})

    else:
        form = AjoutServiceProfessionnel()

    return render(request, 'factotum/serviceProfessionnel_new.html', {'form': form})
