from django.db import models
from service.object import recipe

Recipe = recipe.Recipe


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=False, default="1234")
    pseudo = models.CharField(max_length=100, unique=True)
    favorites = models.ManyToManyField(Recipe, related_name='user_favorite', blank=True)
    madeRecipe = models.IntegerField(default=0, blank=False)
    recipeCreated = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.email
