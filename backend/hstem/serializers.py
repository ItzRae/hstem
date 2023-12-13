from rest_framework import serializers
from .models import Author, Creates, Project, File


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "major", "year"]


class CreatesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(source="name", read_only=True)

    class Meta:
        model = Creates
        fields = ["author", "title"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description", "cohort", "audience"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["name", "title", "is_public", "type", "file"]
