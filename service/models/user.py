from django.db import models
from .recipe import Recipe


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=False, default="1234")
    pseudo = models.CharField(max_length=100, unique=True)
    favorites = models.ManyToManyField(Recipe, related_name='user_favorite')

    # created recipes

    def __str__(self):
        return self.email
