from django import urls
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Furnitures  # Importer la classe Furnitures
import json
from django.views.decorators.csrf import csrf_exempt

def furniture(request,id):
    if request.method == "DELETE":
        Furnitures.objects.filter(id=id).delete()
        return JsonResponse ({'message': 'delete with success!'})

    elif request.method == "PUT":
        Furnitures.objects.filter(id=id).put()  

@csrf_exempt
def furnitures(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        #image = request.POST["image"]
        price = request.POST["price"]
        dimension = request.POST["dimension"]
        typeObject = request.POST["type"]
        color = request.POST["color"]
        condition = request.POST["condition"]
        material = request.POST["material"]

        # Furnitures.objects.create(title=title, description=description, price=price, dimension=dimension,
        #                           type=typeObject, color=color, condition=condition, material=material)

        Furnitures.objects.create(
            title=title, description=description, dimension=dimension)  

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
