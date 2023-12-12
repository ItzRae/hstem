from django.db import models


class Project(models.Model):
    title = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = "hstem_project"
