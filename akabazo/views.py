from rest_framework import viewsets

from .models import *
from .serializers import *

class ProduitViewset(viewsets.ModelViewSet):
    queryset= Produit.objects.all()
    serializer_class=ProduitSerializer

class VenteViewset(viewsets.ModelViewSet):
    queryset= Vente.objects.all()
    serializer_class=VenteSerializer
