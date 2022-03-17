from django import urls
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Furnitures  # Importer la classe Furnitures
from rest_framework.parsers import JSONParser 
from rest_framework import status
from catalog.serializers import FurnituresSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['PUT', 'DELETE'])
def furniture(request, id):
    furniture = Furnitures.objects.get(id=id)
    """ try: 
        furniture = Furnitures.objects.get(id=id) 
    except Furnitures.DoesNotExist: 
        return JsonResponse({'message': 'The furnitures do not exist'}, status=status.HTTP_404_NOT_FOUND) """

    if request.method == "DELETE":
        Furnitures.objects.filter(id=id).delete()
        return JsonResponse({'message': 'delete with success!'})

    elif request.method == "PUT":
        furniture_data = JSONParser().parse(request) 
        furniture_serializer = FurnituresSerializer(furniture, data=furniture_data) 
        if furniture_serializer.is_valid(): 
            furniture_serializer.save() 
            return JsonResponse(furniture_serializer.data) 
        return JsonResponse(furniture_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
def furnitures(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        price = request.POST["price"]
        dimension = request.POST["dimension"]
        typeObject = request.POST["type"]
        color = request.POST["color"]
        condition = request.POST["condition"]
        material = request.POST["material"]

        Furnitures.objects.create(title=title, description=description, price=price, dimension=dimension, type=typeObject, color=color, condition=condition, material=material, img=image)

        

    data = Furnitures.objects.all()  # Récupère tous les enregistrements du tableau


    furnitures = []
    for furniture in data:
        params = {
            'id': int(furniture.id),
            'title': str(furniture.title),
            'description': str(furniture.description),
            'image': str(furniture.img),
            # Transformation de chaque enregistement de type data (données) en type String(chaine de caractères)
            'price': str(furniture.price),
            'dimension': str(furniture.dimension),
            'stock': bool(furniture.stock),
            'type': str(furniture.type),
            'color': str(furniture.color),
            'condition': str(furniture.condition),
            'material': str(furniture.material),
        }
        furnitures.append(params)

    # Retourne la transformation du dessus en format json sans caractères spéciaux (ensure_ascii) avec une indentation de 2 au lieu de 4(par défaut)
    json_str = json.dumps(furnitures, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
