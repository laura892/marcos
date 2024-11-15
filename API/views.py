from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializer
from .models import Libro
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer