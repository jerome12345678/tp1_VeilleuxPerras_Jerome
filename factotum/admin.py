from django.contrib import admin
from .models import User, Service, Soumission, ProfessionnelService

# Register your models here.


class ProfessionnelService_Service_Id(admin.ModelAdmin):
    list_display = ('utilisateur_id', 'service_id')


class ProfessionnelService_Utilisateur_Id(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class Soumission_Utilisateur(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(User)
admin.site.register(Service)
admin.site.register(Soumission)
admin.site.register(ProfessionnelService, ProfessionnelService_Service_Id)




