from django.contrib import admin

#Création de l'API catalog
from .models import Furnitures
admin.site.register(Furnitures)
