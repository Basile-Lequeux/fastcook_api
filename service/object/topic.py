from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)
    createdBy = models.ForeignKey('User', on_delete=models.PROTECT, blank=True, default=None, null=True)
