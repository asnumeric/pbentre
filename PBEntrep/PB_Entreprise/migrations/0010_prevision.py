# Generated by Django 5.0 on 2024-01-06 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0009_tempsarret_date_saisie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.DateField()),
                ('montant_previs', models.IntegerField(default=0)),
            ],
        ),
    ]
