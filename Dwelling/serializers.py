from rest_framework import serializers
from .models import Dwelling, Room, Device, RoomData, Suggestion 


#This is what converts the data to and from JSON format

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('suggestion_id','room_id', 'suggestion',)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomData
        fields = ('data_id', 'room_id', 'co2', 'humidity', 'temperature')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_code','room_id', 'device_name', 'mac_address', 'state', 'energy_used')


class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    data = DataSerializer(many=True, read_only=True)
    suggestion = SuggestionSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('room_id','dwelling_id', 'room_name', 'data', 'devices','suggestion')


class DwellingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Dwelling
        fields = ('id', 'dwelling_code','dwelling_name','has_superAdmin','room')
