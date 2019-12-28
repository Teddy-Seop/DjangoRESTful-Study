from rest_framework import serializers
from .models import posts

class postsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts #모델 설정
        fields = ('id', 'title', 'content', 'writer') #필드 설정

class postsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts #모델 설정
        fields = ('id', 'title', 'content', 'writer') #필드 설정