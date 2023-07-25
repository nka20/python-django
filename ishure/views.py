from rest_framework import viewsets

from .models import *
from .serializers import *

class EleveViewset(viewsets.ModelViewSet):
    queryset= Eleve.objects.all()
    serializer_class=EleveSerializer

class MinervalViewset(viewsets.ModelViewSet):
    queryset= Minerval.objects.all()
    serializer_class=MinervalSerializer

    def perform_create(self,serializer):
        serializer.save(utilisateur=self.request.user)
        return serializer


class ClasseViewset(viewsets.ModelViewSet):
    queryset= Classe.objects.all()
    serializer_class=ClasseSerializer
