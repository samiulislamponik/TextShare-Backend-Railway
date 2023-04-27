from django.db import models

# Create your models here.
class TextSnippet(models.Model):
    content = models.TextField()
    url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.id}: {self.content[:25]}"

