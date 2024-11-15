from django.db import models

# Create your models here.
class Room(models.Model):
 room_number = models.TextField()
 capacity = models.IntegerField()
 available = models.BooleanField()
 description = models.TextField()