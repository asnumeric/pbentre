# Generated by Django 5.0 on 2024-01-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_userprofile_commune'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='1', max_length=20),
            preserve_default=False,
        ),
    ]
