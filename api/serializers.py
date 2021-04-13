from rest_framework import serializers
from service.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class RecipeListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        recipe = [Recipe(**item) for item in validated_data]
        return Recipe.objects.bulk_create(recipe)


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(many=True, queryset=Ingredient.objects.all(), slug_field='name')

    class Meta:
        list_serializer_class = RecipeListSerializer
        model = Recipe
        fields = ['id', 'name', 'url', 'imageUrl', 'totalTime', 'ingredients', 'ingredientsDetail']
        lookup_field = 'name'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'imageUrl']

