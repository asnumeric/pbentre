# Generated by Django 5.0 on 2024-02-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='photo')),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('date_saisie', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='photo')),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('date_saisie', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='video/%y')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
