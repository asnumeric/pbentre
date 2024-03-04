# Generated by Django 5.0 on 2024-01-24 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0010_prevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decaissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_piece', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('montant', models.IntegerField(default=0)),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Encaissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_piece', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=50)),
                ('montant', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Stationnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('date_prochain_paiement', models.DateField()),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_station', to='PB_Entreprise.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Patente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('date_prochain_paiement', models.DateField()),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patantes', to='PB_Entreprise.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Relicat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chauffeur', models.CharField(max_length=50)),
                ('montant', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relicat', to='PB_Entreprise.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Vignette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('date_prochain_paiement', models.DateField()),
                ('date_saisie', models.DateTimeField(auto_now_add=True)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vignettes', to='PB_Entreprise.vehicule')),
            ],
        ),
    ]