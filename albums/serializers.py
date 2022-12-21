from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "user_id", "name", "year"]
        depth = 1

        def create(self, validated_data):
            return Album.objects.create(**validated_data)
