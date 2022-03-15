from django.contrib import admin

# Register your models here.
from .models import Clients

class ClientsAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id', 'pseudo', 'email') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Clients, ClientsAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument