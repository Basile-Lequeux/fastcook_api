from . import serializers
from service.models.ingredient import Ingredient
from service.models.user import User
from service.models.recipe import Recipe
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
            query = Recipe.objects.get_or_create(name=recipe['name'], url=recipe['url'], imageUrl=recipe['imageUrl'],
                                                 totalTime=recipe['totalTime'],
                                                 ingredientsDetail=recipe['ingredientsDetail'])

            if query[1] == True:  # if recipe is created
                for i in recipe['ingredients']:
                    getThisRecipe = Recipe.objects.get(name=recipe['name'])
                    created = Ingredient.objects.get_or_create(name=i.lower())

                    getThisRecipe.ingredients.add(created[0])  # add current ingredient to the current recipe

        return Response('recipes created', status=201)

    def get_queryset(self):
        all_recipe = Recipe.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        ingredient1 = Recipe.objects.none()
        ingredient2 = Recipe.objects.none()
        ingredient3 = Recipe.objects.none()
        ingredient4 = Recipe.objects.none()
        ingredient5 = Recipe.objects.none()
        count = 0

        if ingredient is not None:
            for i in ingredient.split():   #separator between ingredients is a space and not a "&"
                count = count + 1
                if i is not None:
                    if count == 1:
                        ingredient1 = all_recipe.filter(ingredients__name=i)
                    if count == 2:
                        ingredient2 = all_recipe.filter(ingredients__name=i)
                    if count == 3:
                        ingredient3 = all_recipe.filter(ingredients__name=i)
                    if count == 4:
                        ingredient4 = all_recipe.filter(ingredients__name=i)
                    if count == 5:
                        ingredient5 = all_recipe.filter(ingredients__name=i)

        queryset = Recipe.objects.none()
        return queryset.union(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, all=True)

    @action(detail=False, methods=['GET'])
    def get_last_recipes(self, request):
        queryset = Recipe.objects.all().order_by('id')
        serializer = serializers.RecipeSerializer(queryset.reverse()[:5], many=True)

        return Response(serializer.data, status=200)

    @action(detail=False, methods=['GET'])
    def get_random_recipes(self, request):
        queryset = Recipe.objects.all().order_by('?')
        serializer = serializers.RecipeSerializer(queryset.reverse()[:5], many=True)

        return Response(serializer.data, status=200)

    @action(detail=False, methods=['DELETE'])
    def flush_database(self, request):
        allRecipes = Recipe.objects.all()
        allIngredients = Ingredient.objects.all()
        for recipe in allRecipes:
            recipe.delete()
            print(recipe.name + ' deleted')

        for ingr in allIngredients:
            ingr.delete()
            print(ingr.name + ' deleted')

        return Response('all recipes and all ingredients has been deleted', status=200)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
