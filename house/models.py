from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    name = models.CharField(max_length=36)  # name of the room
    # description = models.TextField(max_length=360) #descirption of the room


class House(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class Control(models.Model):
    name = models.CharField(max_length=36)  # name of the room


class Suggestion(models.Model):
    name = models.CharField(max_length=36)  # name of the room
