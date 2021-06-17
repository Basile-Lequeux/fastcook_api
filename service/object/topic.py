from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=100, default="")
