from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Classe(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)

    def __str__(self):
       return f" {self.nom}"

       
class Eleve(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=80)
    classe=models.ForeignKey(Classe,on_delete=models.PROTECT)
    telephone_du_parent=models.IntegerField(unique=True)
    naissance=models.DateField()

    
    def __str__(self):
       return f" {self.nom} {self.prenom}"

class Minerval(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.ForeignKey(Eleve,on_delete=models.PROTECT)
    utilisateur=models.ForeignKey(User,on_delete=models.PROTECT)
    minerval=models.IntegerField(unique=True)
    trimestre=models.CharField(max_length=80)