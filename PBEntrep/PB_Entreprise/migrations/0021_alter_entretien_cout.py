# Generated by Django 5.0 on 2024-02-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PB_Entreprise', '0020_alter_vehicule_duree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entretien',
            name='cout',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
