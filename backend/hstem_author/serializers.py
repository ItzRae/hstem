from rest_framework import serializers
from .models import HstemAuthor

class HstemAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HstemAuthor
        fields = ['name', 'major', 'year']
