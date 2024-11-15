from django.shortcuts import render
from APIREST.models import Room
from APIREST.serializer import RoomSerializer
from rest_framework import viewsets

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
