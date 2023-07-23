# Generated by Django 4.2.3 on 2023-07-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=80)),
                ('telephone_du_parent', models.IntegerField(unique=True)),
                ('naissance', models.DateField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ishure.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Minerval',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('minerval', models.IntegerField(unique=True)),
                ('trimestre', models.CharField(max_length=80)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ishure.eleve')),
            ],
        ),
    ]