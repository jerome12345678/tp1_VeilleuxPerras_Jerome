# Generated by Django 4.1.5 on 2023-02-16 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factotum', '0010_user_telephone_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(default='', max_length=10, validators=[django.core.validators.RegexValidator('^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$', 'Numéro de téléphone invalide')]),
        ),
    ]
