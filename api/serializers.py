from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from service.models.ingredient import Ingredient
from service.models.user import User
from service.models.recipe import Recipe


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'pseudo', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


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
        lookup_field = 'id'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'imageUrl']
        lookup_field = 'id'

