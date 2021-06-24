from django.db import models
from service.object import ingredient

Ingredient = ingredient.Ingredient


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(null=True, blank=True)
    imageUrl = models.URLField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    totalTime = models.CharField(max_length=100, default="0.0")
    ingredientsDetail = models.JSONField(default=dict)
    createdBy = models.ForeignKey('User', on_delete=models.PROTECT, blank=True, default=None, null=True)
    moderate = models.BooleanField(default=True)
    stepList = models.JSONField(null=True)

    def __str__(self):
        return self.name
