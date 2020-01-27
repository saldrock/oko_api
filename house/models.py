from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class House(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class Control(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class Suggestion(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class Devices(models.Model):
    name = models.CharField(max_length=36)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
