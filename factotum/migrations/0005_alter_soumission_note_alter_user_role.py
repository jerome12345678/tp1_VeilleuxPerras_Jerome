# Generated by Django 4.1.5 on 2023-02-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factotum', '0004_alter_soumission_id_service_professionnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soumission',
            name='note',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'utilisateur'), (2, 'professionnel')], default=1),
        ),
    ]