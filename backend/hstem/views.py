from rest_framework import generics
from .models import Author, Creates, Project
from .serializers import AuthorSerializer, CreatesSerializer, ProjectSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreatesList(generics.ListAPIView):
    queryset = Creates.objects.all()
    serializer_class = CreatesSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
