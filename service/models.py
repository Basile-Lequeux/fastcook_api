from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.URLField(null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    imageUrl = models.URLField(null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        return self.name
