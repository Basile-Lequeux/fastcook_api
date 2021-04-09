from . import serializers
from service.models import *
from rest_framework.decorators import api_view
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

    def get_queryset(self):
        queryset = Recipe.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        if ingredient is not None:
            queryset = queryset.filter(ingredients__name=ingredient)
        return queryset

    #lookup_field = 'name'


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
