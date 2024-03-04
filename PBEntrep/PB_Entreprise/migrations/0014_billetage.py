# Generated by Django 5.0 on 2024-01-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0013_decaissement_journalier_encaissement_journalier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billetage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField(choices=[(10000, '10000'), (5000, '5000'), (2000, '2000'), (1000, '1000'), (500, '500'), (200, '200'), (100, '100'), (50, '50'), (25, '25'), (10, '10'), (5, '5')])),
                ('nombre', models.IntegerField()),
                ('type_valeur', models.CharField(choices=[('Billet', 'Billet'), ('Piece', 'Piece')], max_length=10)),
                ('date_saisie', models.DateField(auto_now_add=True)),
            ],
        ),
    ]