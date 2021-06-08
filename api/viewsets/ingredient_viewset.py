from api import serializers
from service.object.ingredient import Ingredient
from rest_framework import viewsets


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
