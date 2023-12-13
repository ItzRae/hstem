from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Creates, Project, File
from .serializers import AuthorSerializer, CreatesSerializer, ProjectSerializer, FileSerializer
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
        creates_serializer = CreatesSerializer(creates)
        files = get_object_or_404(File, title=decoded_title)
        file_serializer = FileSerializer(files)

        response_data = {
            'creates': creates_serializer.data,
            'file': file_serializer.data
        }

        return Response(response_data)


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
