from rest_framework import generics
from rest_framework import serializers

from .models import Yonetmen, Oyuncu, Film


# Yönetmen verilerini JSON formatına dönüştürür
class YonetmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yonetmen
        fields = '__all__'  # Tüm alanları (id, isim, biyografi, fotograf) dahil et


# Oyuncu verilerini JSON formatına dönüştürür
class OyuncuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oyuncu
        fields = '__all__'  # Tüm alanları dahil et


# Film verilerini JSON formatına dönüştürür
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'  # Tüm alanları dahil et
