from django.db import models


class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    major = models.CharField(max_length=255)
    year = models.CharField(max_length=10)

    class Meta:
        db_table = "hstem_author"
