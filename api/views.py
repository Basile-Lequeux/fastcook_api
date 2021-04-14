from . import serializers
from service.models import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'recipe': reverse('recipe-list', request=request, format=format),
        'ingredient': reverse('ingredient-list', request=request, format=format)
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer

    @action(detail=False, methods=['POST'])
    def create_recipes(self, request):
        for recipe in self.request.data:
            query = Recipe.objects.get_or_create(name=recipe['name'].lower(), url=recipe['url'], imageUrl=recipe['imageUrl'],
                                         totalTime=recipe['totalTime'], ingredientsDetail=recipe['ingredientsDetail'])

            for i in recipe['ingredients']:
                getThisRecipe = Recipe.objects.get(name=recipe['name'])
                created = Ingredient.objects.get_or_create(name=i.lower())

                getThisRecipe.ingredients.add(created[0]) # get_or_create return a tuple, here it's -> [ingredients ,
                # true/false]

        return Response('recipes created', status=201)

    def get_queryset(self):
        queryset = Recipe.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        if ingredient is not None:
            queryset = queryset.filter(ingredients__name=ingredient)
        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
