from django.contrib.auth.models import User
from django.db import models


class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True, null=False, default=0)  # ID number of room
    room_name = models.CharField(max_length=50, null=False, default='')  # name of the room
    co2 = models.IntegerField(null=True, default=0)  # CO2 level of the room
    humidity = models.IntegerField(null=True, default=0)  # humidity level of the room


class Dwellings(models.Model):
    dwelling_id = models.IntegerField(primary_key=True, default=0)  # ID number of the dwelling
    dwelling_name = models.CharField(max_length=50, null=False, default='')  # name of the dwelling
    dwelling_code = models.CharField(max_length=8, null=False, default='')  # dwelling code used to sign up to dwelling


class Devices(models.Model):
    device_id = models.IntegerField(primary_key=True, null=False, default=0)  # ID number of device
    device_name = models.CharField(max_length=50, null=False,default='')  # name of device
    #room_id = models.ForeignKey(Rooms.room_id, on_delete=models.CASCADE, related_name='devices', null=False)  # room that the device is in
    status = models.BooleanField(default=False)  # if the device is on or off


class Suggestions(models.Model):
    suggestion_id = models.IntegerField(primary_key=True, null=False, default=0)  # ID number of suggestion
    suggestion_name = models.CharField(max_length=150, null=False, default='')  # suggestion
    weather_suggestion = models.CharField(max_length=150, null=False, default=0)  # weather suggestion
  ##  room_id = models.ForeignKey(Rooms.room_id, on_delete=models.CASCADE,
    #                            null=False)  # the room that the suggestion is for


class Readings(models.Model):
    reading_id = models.IntegerField(primary_key=True, null=False, default=0)  # ID number of suggestion
    #device_id = models.ForeignKey(Devices.device_id, on_delete=models.CASCADE,related_name='device_id')  # device that the reading is from
    reading_type = models.CharField(max_length=50, null=False, default='')  # type of reading eg co2, humidity, heating etc
    reading = models.IntegerField(null=False, default=0)  # the actual reading


class Login(models.Model):
    username = models.CharField(max_length=50, null=False, default='')
    password = models.CharField(max_length=50, null=False, default='')


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=100, null=False, default='')
    #username = models.OneToOneField(Login.username, on_delete=models.CASCADE, related_name='username', max_length=60,null=False)
    first_name = models.CharField(max_length=35, null=False, default='')
    surname = models.CharField(max_length=35, null=False, default='')
   # dwelling_id = models.ForeignKey(Dwellings, on_delete=models.CASCADE, related_name='dwelling_id')
    phone_number = models.CharField(max_length=13, default='')
    incentivisation_choice = models.CharField(max_length=13,default='')


class Progress(models.Model):  # links in with leaderboard
   # username = models.OneToOneField(Login.username, on_delete=models.CASCADE, related_name='username', null=False)
    score = models.IntegerField(blank=True, default=0)  # score to determine ranking on leaderboard
    ranking = models.IntegerField(blank=False, default=100)  # ranking on leaderboard
    money_saved = models.IntegerField(blank=True, default=0)  # money the user has saved
