from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
from .models import posts

class postsList(generics.ListAPIView):
    queryset = posts.objects.all()
    serializer_class = postsListSerializer

class postsDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = posts.objects.all()
    serializer_class = postsDetailSerializer

class postsUpdate(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = posts.objects.all()
    serializer_class = postsListSerializer

class postsDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = posts.objects.all()
    serializer_class = postsListSerializer

class postsCreate(generics.CreateAPIView):
    queryset = posts.objects.all()
    serializer_class = postsCreateSerializer