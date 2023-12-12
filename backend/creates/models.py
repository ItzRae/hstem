from django.db import models


class Creates(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "hstem_create"
