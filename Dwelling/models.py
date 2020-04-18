from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db import migrations


class Dwelling(models.Model):
    dwelling_name   = models.CharField(max_length=50, null=False, default='unnamed dwelling')  # name of the dwelling
    has_superAdmin  = models.BooleanField(default=False)
    dwelling_code   = models.CharField(max_length=8, null=False, default='null')  # dwelling code used to sign up to dwelling

    def __str__(self):
        return self.dwelling_name


class Room(models.Model):
    room_code           = models.CharField(primary_key=True,max_length=30, null=False, default='null')  # dwelling code used to sign up to dwelling
    room_name           = models.CharField(max_length=50, null=False, default='unnamed room')  # name of the room
    related_dwelling    = models.ForeignKey(Dwelling, on_delete=models.CASCADE, related_name='room', default='')

    def __str__(self):
        return self.room_name


class RoomData(models.Model):
    co2             = models.CharField(max_length=10485759, null=False, default='null')  # name of device
    humidity        = models.CharField(max_length=10485759, null=False, default='null')  # name of device
    temperature     = models.CharField(max_length=10485759, null=False, default='null')  # name of device
    related_room    = models.ForeignKey(Room,on_delete=models.CASCADE, related_name='data', default='null')



class Device(models.Model):
    device_code     = models.CharField(primary_key=True, max_length=30, null=False, default='null')  # dwelling code used to sign up to dwelling
    device_name     = models.CharField(max_length=50, null=False, default='unnamed device')  # name of device
    mac_address     = models.CharField(max_length=50, null=False, default='null')  # name of device
    energy_used     = models.IntegerField(default=0)
    state           = models.BooleanField(default=False) # on or off
    room            = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices', default='null')

    def __str__(self):
        return self.device_name
    


class Suggestion(models.Model):
    suggestion      = models.CharField(max_length=150, null=False, default='No Suggestion Calculated')  # suggestion on what to do
    related_room    = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='suggestion', default='null')




