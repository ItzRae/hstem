from rest_framework import serializers
from .models import Author, Creates, Project, File


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "major", "year"]


class CreatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creates
        fields = ["name", "title", "created_at"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "name",
            "is_public",
            "type",
            "uploaded_at",
            "file",
            "title"
        ]
