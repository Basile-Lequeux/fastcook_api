from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email



class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    imageUrl = models.URLField(null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    imageUrl = models.URLField(null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    totalTime = models.CharField(max_length=100, default="0.0") #bug django migrations, we can't use interval...:(
    ingredientsDetail = models.JSONField(default={})

    def __str__(self):
        return self.name
