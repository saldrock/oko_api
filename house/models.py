from django.contrib.auth.models import User
from django.db import models


class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True) #ID number of room
    room_name = models.CharField(max_length=50,null=False)  # name of the room
    co2 = models.IntegerField(null=True) #CO2 level of the room
    humidity = models.IntegerField(null=True) #humidity level of the room

class Dwellings(models.Model):
    dwelling_id = models.IntegerField(primary_key=True) #ID number of the dwelling
    dwelling_name = models.CharField(max_length = 50, null=False) #name of the dwelling
    dwelling_code = models.CharField(max_length=8) #dwelling code used to sign up to dwelling
    
class Devices(models.Model): 
    device_id = models.IntegerField(primary_key=True) #ID number of device
    device_name = models.CharField(max_length=50, null=False) #name of device
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='devices', null=False) #room that the device is in
    status = models.BooleanField(default=False) #if the device is on or off

class Suggestions(models.Model): 
    suggestion_id = models.IntegerField(primary_key=True) #ID number of suggestion
    suggestion_name = models.CharField(max_length = 150, null=False) #suggestion
    weather_suggestion = models.CharField(max_length=150, null=False) #weather suggestion

class Readings(models.Model):  
    reading_id = models.IntegerField(primary_key=True) #ID number of suggestion
    device_id = models.ForeignKey(Devices, on_delete=models.CASCADE, related_name=device_id) #device that the reading is from
    reading_type = models.CharField(max_length=50,null=False) #type of reading eg co2, humidity, heating etc
    reading = models.IntegerField(null=False) # the actual reading

class Login(models.Model):
    username = models.CharField(max_length=50) 
    password = models.CharField(max_length=50) 

class User(models.Model):
    email = models.CharField(primary_key=True, max_length=100, default='')  
    username = models.ForeignKey(Login, on_delete=models.CASCADE, related_name=Login, max_length=60, null=False) 
    first_name = models.CharField(max_length=35,default='')  
    surname = models.CharField(max_length=35, default='')  
    dwelling_id = models.ForeignKey(Dwellings, on_delete=models.CASCADE, related_name=dwelling_id)
    phone_number = models.CharField(max_length=13,default='')
    incentivisation_choice = models.CharField(max_length=13, default='')

class Leaderboard(models.Model):
    username = models.ForeignKey(Login, on_delete=models.CASCADE, related_name= username)
    points = models.IntegerField(blank=True)
    ranking = models.IntegerField(blanK=False)
