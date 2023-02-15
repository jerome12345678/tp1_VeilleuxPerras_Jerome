from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Service(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.nom,)


class User(AbstractUser):
    UTILISATEUR = 1
    PROFESSIONNEL = 2
    ROLE_CHOICES = (
        (UTILISATEUR, 'utilisateur'),
        (PROFESSIONNEL, 'professionnel'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    adresse = models.CharField(max_length=255)
    code_Postal = models.CharField(max_length=6,
                                   validators=[RegexValidator("[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJ-NPRSTV-Z][ ]?|[-]?[0-9][ABCEGHJ-NPRSTV-Z][0-9]",
                                                              'Code postal invalide')],)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="media/")
    Service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s : %s' % (self.username, self.id)


class ProfessionnelService(models.Model):
    taux_horaire = models.IntegerField()
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, default="")
    utilisateur_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return '%s' % (self.utilisateur_id)


class Soumission(models.Model):
    date_planification = models.DateField(auto_now_add=True)
    date_finis = models.DateField()
    description = models.TextField(blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")
    id_service_Professionnel = models.ForeignKey(ProfessionnelService, on_delete=models.CASCADE, null=False, default="")
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    EN_ATTENTE = 1
    ACCEPTEE = 2
    TERMINEE = 3
    ANNULEE = 4
    STATE_CHOICE = (
        (EN_ATTENTE, 'waiting'),
        (ACCEPTEE, 'accepted'),
        (TERMINEE, 'finished'),
        (ANNULEE, 'cancelled')
    )
    role = models.PositiveSmallIntegerField(choices=STATE_CHOICE)

    def __str__(self):
        return '%s : %s : %s : %s : %s' % (self.id_service_Professionnel,
                                           self.utilisateur_id,
                                           self.date_planification,
                                           self.date_finis,
                                           self.note)