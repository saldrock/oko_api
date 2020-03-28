from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db import migrations


class Dwelling(models.Model):
    dwelling_id = models.IntegerField(primary_key=True, default=0)  # ID number of the dwelling
    dwelling_name = models.CharField(max_length=50, null=False, default='')  # name of the dwelling
    dwelling_progress = models.IntegerField(default=0)
    dwelling_code = models.CharField(max_length=8, null=False, default='')  # dwelling code used to sign up to dwelling
    dwelling_members = models.CharField(max_length=50000, null=False,
                                        default='')  # dwelling code used to sign up to dwelling
    dwelling_superUsers = models.CharField(max_length=50000, null=False,
                                           default='')  # dwelling code used to sign up to dwelling

    def __str__(self):
        return self.dwelling_name


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, null=False, default=0)  # ID number of room
    room_name = models.CharField(max_length=50, null=False, default='')  # name of the room
    dwelling_rooms = models.ForeignKey(Dwelling, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.room_name


class RoomData(models.Model):
    co2 = models.CharField(max_length=10485759, null=False, default='')  # name of device
    humidity = models.CharField(max_length=10485759, null=False, default='')  # name of device
    temperature = models.CharField(max_length=10485759, null=False, default='')  # name of device
    light = models.CharField(max_length=10485759, null=False, default='')  # name of device
    rooms_data = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_data', default='')


class Device(models.Model):
    device_name = models.CharField(max_length=50, null=False, default='')  # name of device
    state = models.BooleanField(default=False),  # if the device is on or off
    mac_address = models.CharField(max_length=50, null=False, default='')  # name of device
    room_devices = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices')


class Suggestion(models.Model):
    suggestion = models.CharField(max_length=150, null=False, default=0)  # suggestion on what to do
    room_suggestion = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='suggestion')
