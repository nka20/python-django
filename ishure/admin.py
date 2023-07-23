from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Eleve)
admin.site.register(Minerval)
admin.site.register(Classe)