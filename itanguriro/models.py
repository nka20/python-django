from django.db import models

# Create your models here.
class Amazina(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=80)
    detail=models.TextField(null=True,blank=True)
    telephone=models.IntegerField(unique=True)
    naissance=models.DateField()


