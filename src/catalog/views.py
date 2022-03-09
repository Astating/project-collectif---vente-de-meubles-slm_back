from django.shortcuts import render
from django.http import HttpResponse
from .models import Furnitures #Importer la classe Furnitures
import json

def furnitures(request):
    data = Furnitures.objects.all() #Récupère tous les enregistrements du tableau
    
    furnitures = []
    for furniture in data:
        params = {
            'price':str(furniture.price), #Transformation de chaque enregistement de type data (données) en type String(chaine de caractères)
            'dimension':str(furniture.dimension),
            'stock':bool(furniture.stock),
            'type':str(furniture.type),
            'color':str(furniture.color),
            'condition':str(furniture.condition),
            'material':str(furniture.material),
        }
        furnitures.append(params)
    
    #Retourne la transformation du dessus en format json sans caractères spéciaux (ensure_ascii) avec une indentation de 2 au lieu de 4(par défaut)
    json_str = json.dumps(furnitures, ensure_ascii=False, indent=2) 
    return HttpResponse(json_str)