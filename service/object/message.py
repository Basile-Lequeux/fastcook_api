from django.db import models


class Message(models.Model):
    text = models.TextField()
    topic_related = models.ForeignKey('Topic', on_delete=models.CASCADE, null=False, related_name='message')
    user_related = models.ForeignKey('User', on_delete=models.PROTECT, null=False, related_name='message')

