# Generated by Django 4.2.6 on 2023-12-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='montant',
            field=models.IntegerField(),
        ),
    ]
