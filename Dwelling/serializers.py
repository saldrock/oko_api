from rest_framework import serializers
from .models import Dwelling, Room, Device, RoomData, Suggestion 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('id', 'suggestion', 'room_suggestion')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomData
        fields = ('id', 'co2', 'humidity', 'temperature')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'device_name', 'mac_address', 'state', 'room_devices', 'energy_used')


class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True)
    room_data = DataSerializer(many=True)
    suggestion = SuggestionSerializer(many=True)

    class Meta:
        model = Room
        fields = ('room_id', 'room_name', 'suggestion', 'devices', 'room_data')


class DwellingSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Dwelling
        fields = ('dwelling_name','has_superAdmin' ,'dwelling_code', 'rooms',)
