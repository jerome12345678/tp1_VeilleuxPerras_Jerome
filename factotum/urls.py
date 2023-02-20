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
    path('/soumission/<int:service_id>/new', views.ajout_soumission, name="ajout_soumission"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)