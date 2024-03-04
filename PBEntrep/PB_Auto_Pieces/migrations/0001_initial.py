# Generated by Django 4.2.6 on 2023-12-01 17:26

import PB_Auto_Pieces.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.DecimalField(decimal_places=2, default='0.0', max_digits=10)),
                ('stautus_paiement', models.BooleanField(default=False)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('status_prod', models.CharField(choices=[('traiter', 'Traitement'), ('expedier', 'Expedier'), ('livrer', 'Livrer')], default='Traitement', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Panier des Commandes',
            },
        ),
        migrations.CreateModel(
            name='CategoProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=22, max_length=30, prefix='cat', unique=True)),
                ('libelle', models.CharField(default='mecano', max_length=30)),
                ('image', models.ImageField(default='catego_prod.jpg', upload_to='category_prod')),
            ],
            options={
                'verbose_name_plural': 'Categories Produits',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=22, max_length=30, prefix='ven', unique=True)),
                ('Libelle', models.CharField(default='Produit', max_length=10)),
                ('image', models.ImageField(default='produit.jpg', upload_to=PB_Auto_Pieces.models.user_directory_path)),
                ('description', models.TextField(blank=True, default='La qualité produit', null=True)),
                ('prix', models.DecimalField(decimal_places=2, default='0.0', max_digits=999)),
                ('ancien_prix', models.DecimalField(decimal_places=2, default='0.0', max_digits=999)),
                ('Specification', models.TextField(blank=True, null=True)),
                ('status_prod', models.CharField(choices=[('projet', 'Projet'), ('desactiver', 'Desactiver'), ('rejeter', 'Rejeter'), ('en_revision', 'En_revision'), ('publier', 'Publier')], default='En revision', max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('en_stock', models.BooleanField(default=True)),
                ('en_vedette', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=22, max_length=10, prefix='sku', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mis_a_jour', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PB_Auto_Pieces.categoprod')),
            ],
            options={
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=22, max_length=30, prefix='ven', unique=True)),
                ('nom', models.CharField(default='Produit', max_length=10)),
                ('image', models.ImageField(default='vendeur.jpg', upload_to=PB_Auto_Pieces.models.user_directory_path)),
                ('description', models.TextField(blank=True, default='Le meilleur', null=True)),
                ('address', models.CharField(default=' 225 Rue principale', max_length=50)),
                ('Contact', models.CharField(default=' +225 00 00 00 00 00', max_length=50)),
                ('achat_a_temps', models.CharField(default='100', max_length=50)),
                ('jour_de_retour', models.CharField(default='100', max_length=50)),
                ('period_garentie', models.CharField(default='100', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendeurs',
            },
        ),
        migrations.CreateModel(
            name='ProduitImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='product.jpg', upload_to='product_img')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PB_Auto_Pieces.produit')),
            ],
            options={
                'verbose_name_plural': 'Image Produit',
            },
        ),
        migrations.AddField(
            model_name='produit',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PB_Auto_Pieces.tags'),
        ),
        migrations.AddField(
            model_name='produit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revue', models.TextField()),
                ('classement', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PB_Auto_Pieces.produit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Produits Revus',
            },
        ),
        migrations.CreateModel(
            name='ListeSouhaite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PB_Auto_Pieces.produit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Liste Souhaite',
            },
        ),
        migrations.CreateModel(
            name='CartOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_prod', models.CharField(max_length=30)),
                ('facture_no', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('qte', models.IntegerField(default=0)),
                ('prix', models.DecimalField(decimal_places=2, default='0.0', max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default='0.0', max_digits=10)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PB_Auto_Pieces.cartorder')),
            ],
            options={
                'verbose_name_plural': 'Panier article commandé ',
            },
        ),
        migrations.CreateModel(
            name='Addresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
