from rest_framework import serializers
from .models import Creates


class CreatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creates
        fields = ["name", "title", "created_at"]
