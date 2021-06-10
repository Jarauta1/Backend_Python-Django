from rest_framework import serializers

from .models import SuperHeroe

class SuperHeroeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuperHeroe
        fields = ('id', 'name', 'alias')