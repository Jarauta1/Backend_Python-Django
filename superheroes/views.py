from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SuperHeroeSerializer
from .models import SuperHeroe

# Create your views here.
class SuperHeroeViewSet(viewsets.ModelViewSet):
    queryset = SuperHeroe.objects.all().order_by('id')
    serializer_class = SuperHeroeSerializer