from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'recipe', views.RecipeViewSet, basename='recipe')
router.register(r'ingredient', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

