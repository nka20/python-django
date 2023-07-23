"""
URL configuration for umwimenyerezo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [ 
path('',home,name='home'),
path('guteranya/<n1>/<n2>/',guteranya,name='sawa'),
path('igisoro/<n1>/',igisoro,name='table'),
path('kugabura/<n1>/<n2>/<n3>',kugabura,name='divisible'),
path('premier/<n1>/<n2>/',premier,name='divisible'),
]
