# Generated by Django 4.1.5 on 2023-02-13 19:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factotum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='soumission',
            old_name='finished_date',
            new_name='date_finis',
        ),
        migrations.RenameField(
            model_name='soumission',
            old_name='planification_date',
            new_name='date_planification',
        ),
        migrations.RenameField(
            model_name='soumission',
            old_name='professionnal_service_id',
            new_name='id_service_Professionnel',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postal_Code',
            new_name='code_Postal',
        ),
        migrations.RemoveField(
            model_name='soumission',
            name='user',
        ),
        migrations.AddField(
            model_name='soumission',
            name='utilisateur',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProfessionnelService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux_horaire', models.IntegerField()),
                ('service_id', models.ManyToManyField(to='factotum.service')),
                ('utilisateur_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
