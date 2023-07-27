# Generated by Django 4.2.3 on 2023-07-27 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prix_unitaire', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prix_total', models.IntegerField(unique=True)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='akabazo.produit')),
            ],
        ),
    ]
