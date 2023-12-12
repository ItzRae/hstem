from django.db import models


class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    major = models.CharField(max_length=255)
    year = models.CharField(max_length=10)

    class Meta:
        db_table = "hstem_author"


class Creates(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "hstem_create"


class Project(models.Model):
    title = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = "hstem_project"


class File(models.Model):
    # "name", "is_public", "extension", "uploaded_at", "file", "title"
    name = models.CharField(max_length=100, primary_key=True)
    is_public = models.BooleanField()
    type = models.CharField(max_length=50)  # TODO: Rename
    uploaded_at = models.DateTimeField()
    file = models.CharField(max_length=255)  # TODO: Rename
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "hstem_file"
