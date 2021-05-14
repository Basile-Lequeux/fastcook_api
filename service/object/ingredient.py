from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    imageUrl = models.URLField(null=True)

    def __str__(self):
        return self.name
