from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Room, House, Control, Suggestion, Devices
from django.contrib.auth.models import User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ('id', 'name')


class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True)
    class Meta:
        model = Room
        fields = ('id', 'name', 'device')




class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'name')


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'name')


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
