from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    name = models.CharField(max_length=36) #name of the room
    period = models.DateTimeField() #length of time
    type = models.CharField(max_Length=36)#type of data they want