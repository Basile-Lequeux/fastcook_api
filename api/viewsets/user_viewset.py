from rest_framework import viewsets
from service.object.user import User
from api import serializers
from service.object.recipe import Recipe
from rest_framework.response import Response
from rest_framework.decorators import api_view, action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=['PUT'])
    def put_favorite(self, request):
        query = self.request.data
        user = User.objects.get(id=query['id'])
        favorite = Recipe.objects.get(id=query['favorite'])

        check_favorite = User.objects.filter(favorites__id=favorite.id).values().filter(id=user.id).exists()
        serialize = serializers.UserSerializer(user)
        if check_favorite:
            user.favorites.remove(favorite)
            return Response(serialize.data, status=200)
        else:
            user.favorites.add(favorite)
            return Response(serialize.data, status=200)

    @action(detail=False, methods=['GET'])
    def connection(self, request):
        login = self.request.query_params.get('login', None)
        password = self.request.query_params.get('password', None)
        user = User.objects.get(email=login)
        if user.password == password:
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data, status=200)

        return Response("wrong email or password", status=400)

    @action(detail=False, methods=['GET'])
    def detail_favorite(self, request):
        user_id = self.request.query_params.get('id', None)
        if user_id:
            user = User.objects.get(id=user_id)
            queryset = user.favorites.all()
            serializer = serializers.RecipeSerializer(queryset, many=True)
            return Response(serializer.data, status=200)

        return Response(status=404)

    @action(detail=False, methods=['PUT', 'POST'])
    def edit_profile(self, request):
        query = self.request.data
        user_id = query['id']
        password = query['password']

        if user_id:
            user = User.objects.get(id=user_id)
            if query['pseudo'] != "":
                user.pseudo = query['pseudo']
            if user.password == password:
                if query['new_password'] != "":
                    user.password = query['new_password']

            user.save()
            return Response(status=200)

    @action(detail=False, methods=['PUT'])
    def increment_made_recipe(self, request):
        query = self.request.data

        user_id = query['id']
        if user_id:
            user = User.objects.get(id=user_id)
            user.madeRecipe = user.madeRecipe + 1
            user.save()
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data, status=200)

        return Response(status=404)
