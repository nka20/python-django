from rest_framework import serializers
from .models import *



class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"
        read_only_fields = ['utilisateur']
class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = "__all__"
        read_only_fields = ['utilisateur']
class MinervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minerval
        #fields = "nom","trimestre","minerval","utilisateur",
        fields = "__all__"
        read_only_fields = ['utilisateur']