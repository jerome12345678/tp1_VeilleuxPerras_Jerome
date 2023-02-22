from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profil/', views.profil, name="profil"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name="register"),
    path('professionnel/list/', views.liste_professionnel, name="liste_professionnel"),
    path('professionnel_service/new/<int:user_id>', views.ajout_service, name="ajout_service"),
    path('soumission/<int:service_id>/new', views.ajout_soumission, name="ajout_soumission"),
    path('soumission/<int:soumission_id>/accepter', views.accepter_soumission, name="accepter_soumission"),
    path('soumission/<int:soumission_id>/terminer', views.terminer_soumission, name="terminer_soumission"),
    path('soumission/<int:soumission_id>/annuler', views.annuler_soumission, name="annuler_soumission"),
    path('soumission/<int:soumission_id>/noter', views.noter_soumission, name="noter_soumission"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)