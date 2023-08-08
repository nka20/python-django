from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

router = routers.DefaultRouter()

router.register("ingenzi", IngenziViewset)
router.register("urugendo", UrugendoViewset)
router.register("itike", ItikeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',TokenObtainPainView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
