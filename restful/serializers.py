from rest_framework import serializers
from .models import container

class containerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = container
        fields = ('c_id', 'entry', 'output', 'arrival', 'departure',
                  'type', 'load', 'weight', 'temparature', 'humidity')

class containerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = container
        fields = ('c_id', 'entry', 'output', 'arrival', 'departure',
                  'type', 'load', 'weight', 'temparature', 'humidity')

class containerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = container
        fields = ('c_id', 'entry', 'output', 'arrival', 'departure',
                  'type', 'load', 'weight', 'temparature', 'humidity')
