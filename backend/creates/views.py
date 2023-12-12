from rest_framework import generics
from .models import Creates
from .serializers import CreatesSerializer


class CreatesList(generics.ListAPIView):
    queryset = Creates.objects.all()
    serializer_class = CreatesSerializer
