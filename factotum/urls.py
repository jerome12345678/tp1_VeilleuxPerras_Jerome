from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profil/', views.profil, name="profil"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)