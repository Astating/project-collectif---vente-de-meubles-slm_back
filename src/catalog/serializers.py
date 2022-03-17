from rest_framework import serializers 
from catalog.models import Furnitures


class FurnituresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Furnitures
        fields = ('id', 'title', 'description', 'price', 'dimension', 'stock', 'img', 'material', 'condition', 'color', 'type')
