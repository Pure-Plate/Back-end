from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model.
    """
    class Meta:
        model = Favorite
        fields = ['user', 'restaurant']  # Fields to be included in the serialized output
