from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Creates, Project
from .serializers import AuthorSerializer, CreatesSerializer, ProjectSerializer
from urllib.parse import unquote
from django.shortcuts import get_object_or_404


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreatesList(generics.ListAPIView):
    queryset = Creates.objects.all()
    serializer_class = CreatesSerializer



class CreatesDetailView(APIView):
    def get(self, request, title):
        decoded_title = unquote(title)
        creates = get_object_or_404(Creates, title=decoded_title)
        serializer = CreatesSerializer(creates)
        return Response(serializer.data)


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
