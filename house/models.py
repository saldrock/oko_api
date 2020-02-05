from django.contrib.auth.models import User
from django.db import models


# User stuff Neve
class Room(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class House(models.Model):
    name = models.CharField(max_length=36)  # name of the room
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rooms', null=True)


class Devices(models.Model):  # Bernie
    name = models.CharField(max_length=36)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices', null=True)


class Control(models.Model):  # Probably not us, controllng smart devices
    name = models.CharField(max_length=36)  # name of the room


class Suggestion(models.Model):  # Harvie
    name = models.CharField(max_length=36)  # name of the room


class Readings(models.Model):  # Neve, from the house
    name = models.CharField(max_length=36)
