from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Room
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    model = Room
    fields = ('id', 'name', 'period')