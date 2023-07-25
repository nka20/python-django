from django.urls import path, include
from rest_framework import routers
from .views import *

routers = routers.DefaultRouter()

routers.register("ingenzi",IngenziViewset)
routers.register("urugendo",UrugendoViewset)
routers.register("itike",ItikeViewset)

urlpatterns = [
    path("", include(routers.urls)),
    path('api-auth/', include('rest_framework.urls')),#pour authentifier et se deconnecter
]
