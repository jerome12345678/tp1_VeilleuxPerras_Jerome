from django.shortcuts import render, redirect
from .forms import RegisterForm, SearchProfessionnal, AjoutServiceProfessionnel
from .models import User, Soumission, ProfessionnelService, Service
from django.contrib import messages
from tp1_VeilleuxPerras_Jerome import settings
import urllib.request
import json


# Create your views here.
def index(request):
    return render(request, 'factotum/base.html')


def profil(request):
    soumissions = Soumission.objects.all()
    soumission = []
    for item in soumissions:
        if item.id_service_Professionnel.utilisateur_id.id == request.user.id:
            soumission.append(item)

    services = ProfessionnelService.objects.filter(utilisateur_id=request.user.id)

    return render(request, 'factotum/profil_details.html', {'soumissions': soumission, 'user_services': services})


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
                res = urllib.request.urlopen(
                    'http://www.zipcodeapi.com/rest/v2/CA/' + api_key + '/distance.json/' + code_postal.replace(
                        ' ', '') + '/' + pro.utilisateur_id.code_Postal.replace(' ', '') + '/km')
                json_data = json.load(res)
                distance = json_data

                result = (
                    (pro, distance)
                )

                list_pro.append(result)

            return render(request, 'factotum/professionnel_list.html', {'professionnels': list_pro})

    else:
        form = SearchProfessionnal()

    return render(request, 'factotum/recherche.html', {'form': form, 'services': allServices})


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


def ajout_soumission(request):
    return render(request, 'factotum/soumission_new.html')
