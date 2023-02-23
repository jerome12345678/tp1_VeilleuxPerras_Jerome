import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, SearchProfessionnal, AjoutServiceProfessionnel, AjoutSoumission
from .models import User, Soumission, ProfessionnelService, Service
from django.contrib import messages
from tp1_VeilleuxPerras_Jerome import settings
import urllib.request
import json


# Vue de départ, initialise la base sur quoi tout les templates seront redirigé
def index(request):
    return render(request, 'factotum/base.html')


# Vue pour la page de profil d'un utilisateur
@login_required(login_url='/accounts/login/')
def profil(request):
    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    soumissions_demande = Soumission.objects.filter(utilisateur_id=request.user.id)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission,
                                                            'soumissionsDemande': soumissions_demande,
                                                            'user_services': services})


# Vue pour créer un nouveau compte
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


# Vue qui affiche la liste de professionnel à la suite d'une recherche
def liste_professionnel(request):
    list_pro = []
    api_key = settings.API_KEY
    allServices = Service.objects.all()

    if request.method == "POST":
        form = SearchProfessionnal(request.POST)
        a = request.POST['services']
        service = Service.objects.get(id=a)

        code_postal = request.POST['code_postal']

        if form.is_valid():
            servicesPro = ProfessionnelService.objects.filter(service_id=service)

            for pro in servicesPro:

                notes = Soumission.objects.filter(id_service_Professionnel=pro.utilisateur_id.id)
                total = 0
                for proNote in notes:
                    total = total + proNote.note

                res = urllib.request.urlopen('http://www.zipcodeapi.com/rest/v2/CA/' + api_key +
                                             '/distance.json/' + code_postal.replace(' ', '') +
                                             '/' + pro.utilisateur_id.code_Postal.replace(' ', '') + '/km')
                json_data = json.load(res)

                result = (
                    (pro, json_data['distance'], total)
                )

                list_pro.append(result)
                list_pro.sort(key=lambda a: a[1])

            return render(request, 'factotum/professionnel_list.html',
                          {'professionnels': list_pro})

    else:
        form = SearchProfessionnal()

    return render(request, 'factotum/recherche.html', {'form': form, 'services': allServices})


# Vue pour ajouter un service à un utilisateur professionnel
@login_required(login_url='/accounts/login/')
def ajout_service(request, user_id):
    allServices = Service.objects.all()
    if request.method == "POST":
        form = AjoutServiceProfessionnel(request.POST)
        a = request.POST['services']
        taux_horaire = request.POST['taux_horaire']

        if form.is_valid():
            service = Service.objects.get(id=a)
            user = User.objects.get(id=request.user.id)
            ProfessionnelService.objects.create(taux_horaire=taux_horaire, service_id=service,
                                                utilisateur_id=user)
            services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)
            return render(request, 'factotum/profil_details.html', {'user_services': services})

    else:
        form = AjoutServiceProfessionnel()

    return render(request, 'factotum/serviceProfessionnel_new.html', {'form': form, 'allServices': allServices})


# Vue pour ajouter créer une demande de soumission d'un utilisateur à un professionnel
@login_required(login_url='/accounts/login/')
def ajout_soumission(request, service_id):
    if request.method == "POST":
        form = AjoutSoumission(request.POST)

        if form.is_valid():

            pro = ProfessionnelService.objects.get(utilisateur_id=service_id)
            date = form.cleaned_data['date_planification']
            description = form.cleaned_data['description']

            Soumission.objects.create(description=description, etat=1,
                                      date_planification=date, id_service_Professionnel=pro,
                                      utilisateur_id=request.user.id, note=0)

        services = Service.objects.all()
        return render(request, 'factotum/recherche.html', {'services': services})

    else:
        form = AjoutSoumission()

    pro = ProfessionnelService.objects.get(utilisateur_id=service_id)
    return render(request, 'factotum/soumission_new.html', {'form': form, 'pro': pro})


# Vue pour changer l'état d'une soumission à 'Accepter'
def accepter_soumission(request, soumission_id):
    soumission = Soumission.objects.get(id=soumission_id)
    soumission.etat = 2
    soumission.save()

    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    soumissionsDemande = Soumission.objects.filter(utilisateur_id=request.user.id)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission,
                                                            'soumissionsDemande': soumissionsDemande,
                                                            'user_services': services})


# Vue pour changer l'état d'une soumission à 'Terminer'
def terminer_soumission(request, soumission_id):
    soumission = Soumission.objects.get(id=soumission_id)
    soumission.etat = 3
    soumission.date_finis = datetime.date.today()
    soumission.save()

    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    soumissionsDemande = Soumission.objects.filter(utilisateur_id=request.user.id)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission,
                                                            'soumissionsDemande': soumissionsDemande,
                                                            'user_services': services})


# Vue pour changer l'état d'une soumission à Annuler
def annuler_soumission(request, soumission_id):
    soumission = Soumission.objects.get(id=soumission_id)
    soumission.etat = 4
    soumission.save()

    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    soumissionsDemande = Soumission.objects.filter(utilisateur_id=request.user.id)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission,
                                                            'soumissionsDemande': soumissionsDemande,
                                                            'user_services': services})

# Vue pour noter une soumission lorsque terminé (incomplète)
def noter_soumission(request, soumission_id):
    soumission = Soumission.objects.get(id=soumission_id)
    soumission.note = soumission.note + 1
    soumission.save()

    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    soumissionsDemande = Soumission.objects.filter(utilisateur_id=request.user.id)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission,
                                                            'soumissionsDemande': soumissionsDemande,
                                                            'user_services': services})
