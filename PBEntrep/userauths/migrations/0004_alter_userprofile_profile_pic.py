# Generated by Django 5.0 on 2024-01-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_user_gender_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='PBEntrep/media/profi_h.png', upload_to='profile/'),
        ),
    ]
