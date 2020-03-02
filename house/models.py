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
    status = models.BooleanField(default=False)


class Control(models.Model):  # Probably not us, controllng smart devices
    name = models.CharField(max_length=36)  # name of the room


class Suggestion(models.Model):  # Harvie
    name = models.CharField(max_length=36)  # name of the room


class Readings(models.Model):  # Neve, from the house
    name = models.CharField(max_length=36)

class Login(models.Model):
    username = models.CharField(max_length=50) #primary key
    password = models.CharField(max_length=50) #required

    #lass
    #User(models.Model):
    email = models.CharField(max_length=75, default='')  # primary key
    username = models.CharField(max_length=60, default='')  # foregin key
    first_name = models.CharField(max_length=35,default='')  # required
    surname = models.CharField(max_length=35, default='')  # required
    dwelling_id = models.CharField(max_length=16, default='')  # need multiple fields and foregin key
    phone_number = models.CharField(max_length=13,default='')
    incentivisation_choice = models.CharField(max_length=13, default='')


class Dwelling(models.Model):
    dwelling_id = models.CharField(max_length=16, default='XXXXX')  # primary key
    dwelling_name = models.CharField(max_length=50,default='')  # required
    users = models.CharField(max_length=50,default='')


class Device(models.Model):
    device_id = models.CharField(max_length=60, default='')  # primary key
    device_name = models.CharField(max_length=50, default='')  # required
    device_room = models.CharField(max_length=50, default='')  # required
    device_status = models.BooleanField(default=False)


class Suggestion(models.Model):
    suggestion_id = models.IntegerField(blank=True, null=True)# primary key
    suggestion = models.CharField(max_length=50, default='')
    weather_suggestion = models.CharField(max_length=50,default='')


class Reading(models.Model):
    reading_id = models.IntegerField(blank=True, null=True)  # primary key
    # device_id = foregin key
    reading_type = models.CharField(max_length=50,default='')
    reading = models.IntegerField(blank=True, null=True)
