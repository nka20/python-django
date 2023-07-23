from rest_framework import serializers
from .models import *



class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"
class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleve
        fields = "__all__"

class MinervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minerval
        fields = "__all__"