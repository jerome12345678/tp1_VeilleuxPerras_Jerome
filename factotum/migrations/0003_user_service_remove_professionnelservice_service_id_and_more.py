# Generated by Django 4.1.5 on 2023-02-13 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factotum', '0002_service_rename_finished_date_soumission_date_finis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='factotum.service'),
        ),
        migrations.RemoveField(
            model_name='professionnelservice',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='professionnelservice',
            name='utilisateur_id',
        ),
        migrations.RemoveField(
            model_name='soumission',
            name='utilisateur',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'user'), (2, 'prof')], default=1),
        ),
        migrations.AddField(
            model_name='professionnelservice',
            name='service_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='factotum.service'),
        ),
        migrations.AddField(
            model_name='professionnelservice',
            name='utilisateur_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='soumission',
            name='utilisateur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]