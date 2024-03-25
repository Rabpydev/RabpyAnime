from rest_framework import serializers
from .models import Character, Anime, Category

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'name']

class CharacterSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'description', 'gender', 'age', 'role', 'weapon', 'ability', 'anime']