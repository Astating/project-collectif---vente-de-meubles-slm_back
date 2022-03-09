from django.shortcuts import render
from django.http import HttpResponse
from .models import Furnitures #Importer la classe Furnitures
import json

def furnitures(request):
    data = Furnitures.objects.all() #Récupère tous les enregistrements du tableau
    params = {
            'price':str(data[0].price), #Puisque chaque enregistrement est de type data, transtypez-le en type String
            'dimension':str(data[0].dimension),
            'stock':bool(data[0].stock),
            'type':str(data[0].type),
            'color':str(data[0].color),
            'condition':str(data[0].condition),
            'material':str(data[0].material),
        }
    json_str = json.dumps(params, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
