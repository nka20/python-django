# Generated by Django 4.2.3 on 2023-08-04 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urugendo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itike',
            name='uwayimuhaye',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itike',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
