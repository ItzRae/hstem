from rest_framework import generics
from .models import HstemAuthor
from .serializers import HstemAuthorSerializer

class HstemAuthorList(generics.ListAPIView):
    queryset = HstemAuthor.objects.all()
    serializer_class = HstemAuthorSerializer