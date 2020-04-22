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
        fields = ('id','related_room', 'suggestion',)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomData
        fields = ('related_room', 'co2', 'humidity', 'temperature')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        # fields = ('device_code','room', 'device_name', 'mac_address', 'state', 'energy_used')
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    data = DataSerializer(many=True, read_only=True)
    suggestion = SuggestionSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('room_code','related_dwelling', 'room_name', 'data', 'devices','suggestion')


class DwellingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Dwelling
        fields = ('id', 'dwelling_code','dwelling_name','has_superAdmin','room')
