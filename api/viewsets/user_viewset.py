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
        if check_favorite:
            user.favorites.remove(favorite)
            return Response("favorite removed", status=200)
        else:
            user.favorites.add(favorite)
            return Response("favorite added", status=200)

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
        query = self.request.data
        user = User.objects.get(id=query['id'])
        queryset = user.favorites.all()
        serializer = serializers.RecipeSerializer(queryset, many=True)

        return Response(serializer.data, status=200)


