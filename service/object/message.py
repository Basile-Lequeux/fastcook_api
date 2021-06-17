from django.db import models


class Message(models.Model):
    text = models.TextField()
    topic_id = models.ForeignKey('Topic', on_delete=models.CASCADE, null=False, related_name='message')
    author = models.ForeignKey('User', on_delete=models.PROTECT, null=False, related_name='message')

