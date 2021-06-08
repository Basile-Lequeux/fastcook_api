from django.urls import path, include
from api.viewsets import user_viewset
from api.viewsets import recipe_viewset
from api.viewsets import ingredient_viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', user_viewset.UserViewSet)
router.register(r'recipe', recipe_viewset.RecipeViewSet)
router.register(r'ingredient', ingredient_viewset.IngredientViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

