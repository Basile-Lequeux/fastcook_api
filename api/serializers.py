from rest_framework import serializers
from service.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(many=True, queryset=Ingredient.objects.all(), slug_field='name')

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'url', 'imageUrl', 'ingredients']
        lookup_field = 'name'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'imageUrl']
