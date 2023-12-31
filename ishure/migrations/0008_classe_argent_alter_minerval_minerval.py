# Generated by Django 4.2.3 on 2023-08-04 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ishure', '0007_classe_utilisateur_eleve_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='argent',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='minerval',
            name='minerval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ishure.classe'),
        ),
    ]
