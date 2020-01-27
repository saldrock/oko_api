from django.contrib.auth.models import User
from django.db import models

class house(models.Model)
    no_of_rooms = models.IntegerField()

    #all calulated
    def avgTemp(self):
    def avgHum(self):
    def avgCo2(self):

class Room(models.Model): #Our room model
    name = models.CharField(max_length=36)  # name of the room

    #all calcuated
    def humidity(self):
    def tempurature(self):
    def Co2(self):


class DataReport(models.Model):#data reporting model
    def lifetime(self):


class Control(models.Model): #device control model (mabye handled by react???)
