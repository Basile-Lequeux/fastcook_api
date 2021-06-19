from api import serializers
from service.object.ingredient import Ingredient
from service.object.recipe import Recipe
from service.object.user import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    @action(detail=False, methods=['POST'])
    def post_recipes(self, request):
        for recipe in self.request.data:
            query = Recipe.objects.get_or_create(name=recipe['name'], url=recipe['url'], imageUrl=recipe['imageUrl'],
                                                 totalTime=recipe['totalTime'],
                                                 ingredientsDetail=recipe['ingredientsDetail'])

            if query[1]:  # if recipe is created
                for i in recipe['ingredients']:
                    get_this_recipe = Recipe.objects.get(name=recipe['name'])
                    created = Ingredient.objects.get_or_create(name=i.lower())

                    get_this_recipe.ingredients.add(created[0])  # add current ingredient to the current recipe

        return Response('recipes created', status=201)

    @action(detail=False, methods=['POST'])
    def create_recipe(self, request):
        request = self.request.data
        recipe = request['recipe']
        user_id = request['userid']
        user = User.objects.get(id=user_id)

        Recipe.objects.get_or_create(name=recipe['name'], url=recipe['url'], imageUrl=recipe['imageUrl'],
                                     totalTime=recipe['totalTime'],
                                     ingredientsDetail=recipe['ingredientsDetail'], createdBy=user, moderate=False)

        new_recipe = Recipe.objects.get(name=recipe['name'])

        serialize = serializers.RecipeSerializer(new_recipe, many=False)

        return Response(serialize.data, status=200)

    @action(detail=False, methods=['GET'])
    def get_non_moderate_recipe(self, request):
        query = Recipe.objects.all().filter(moderate=False)

        serializer = serializers.RecipeSerializer(query, many=True)

        return Response(serializer.data, status=200)

    @action(detail=False, methods=['GET'])
    def search_by_ingredient(self, request):
        all_recipe = Recipe.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        ingredient1 = Recipe.objects.none()
        ingredient2 = Recipe.objects.none()
        ingredient3 = Recipe.objects.none()
        ingredient4 = Recipe.objects.none()
        ingredient5 = Recipe.objects.none()
        count = 0

        if ingredient is not None:
            for i in ingredient.split():  # separator between ingredients is a space and not a "&"
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
        serializer = serializers.RecipeSerializer(
            queryset.union(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5), many=True)
        return Response(serializer.data, status=200)

    @action(detail=False, methods=['GET'])
    def get_by_name(self, request):
        name = self.request.query_params.get('name', None)
        if name:
            if len(name) > 3:
                queryset = Recipe.objects.filter(name__icontains=name)
                serializer = serializers.RecipeSerializer(queryset, many=True)
                return Response(serializer.data, status=200)
        return Response('we can\'t found any recipe with these info please retry', status=404)

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
        all_recipes = Recipe.objects.all()
        all_ingredients = Ingredient.objects.all()
        for recipe in all_recipes:
            recipe.delete()
            print(recipe.name + ' deleted')

        for ingr in all_ingredients:
            ingr.delete()
            print(ingr.name + ' deleted')

        return Response('all recipes and all ingredients has been deleted', status=200)
