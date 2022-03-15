from django.contrib import admin

#Création de l'API catalog
from .models import Furnitures
class FurnituresAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id', 'title', 'stock') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Furnitures, FurnituresAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument