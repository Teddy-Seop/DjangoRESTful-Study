from django.shortcuts import render
from rest_framework import viewsets
from .serializers import postsSerializer
from .models import posts

class postsViewSet(viewsets.ModelViewSet):
    queryset = posts.objects.all()
    serializer_class = postsSerializer