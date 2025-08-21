from django.db import models

# Create your models here.

from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
