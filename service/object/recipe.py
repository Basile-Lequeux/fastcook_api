from django.db import models
from .ingredient import *


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    imageUrl = models.URLField(null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    totalTime = models.CharField(max_length=100, default="0.0")  # bug django migrations, we can't use interval...:(
    ingredientsDetail = models.JSONField(default={})
    createdBy = models.ForeignKey('User', on_delete=models.PROTECT, blank=True, default=None, null=True)
    # IsCustom?

    def __str__(self):
        return self.name
