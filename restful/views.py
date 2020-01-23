from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import container

class containerList(generics.ListAPIView):
    queryset = container.objects.all()
    serializer_class = containerListSerializer

class containerDetail(generics.RetrieveAPIView):
    lookup_field = 'c_id'
    queryset = container.objects.all()
    serializer_class = containerDetailSerializer

    # def put(self, request):
    #     snippet = self.get_objects.all()
    #     serializer = containerCreate(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request):
    #     snippet = self.get_object.all()
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class containerUpdate(generics.UpdateAPIView):
    lookup_field = 'c_id'
    queryset = container.objects.all()
    serializer_class = containerListSerializer

class containerDelete(generics.DestroyAPIView):
    lookup_field = 'c_id'
    queryset = container.objects.all()
    serializer_class = containerListSerializer

class containerCreate(generics.CreateAPIView):
    queryset = container.objects.all()
    serializer_class = containerCreateSerializer
