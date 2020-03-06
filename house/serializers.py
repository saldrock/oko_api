from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Rooms, Suggestions, Login, Dwellings, Devices, Readings, Progress
from django.contrib.auth.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'username', 'password')


class RoomSerializer(serializers.ModelSerializer):
    # devices = DeviceSerializer(many=True)
    class Meta:
        model = Rooms
        fields = ('id', 'room_ID', 'room_name', 'Co2', 'humidity', 'temperature')


class DwellingSerializer(serializers.ModelSerializer):
    # rooms = DwellingSerializer(many=True)
    class Meta:
        model = Dwellings
        fields = ('id', 'dwelling_id', 'dwelling_name', 'dwelling_code')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ('id', 'device_id', 'device_name', 'room_id', 'status')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = ('id', 'suggestion_id', 'suggestion_name', 'weather_suggestion')


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readings
        fields = ('reading_id', 'device_id', 'reading_type', 'reading')


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('username', 'score', 'ranking', 'money_saved')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
