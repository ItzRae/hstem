from django.db import models


class Project(models.Model):
    imageUrl = models.URLField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField()
    extension = models.CharField(max_length=10, default='')  # Provide a default value or set null=True
