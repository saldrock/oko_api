from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Room, DataType, TimePeriod
from django.contrib.auth.models import User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('id', 'room', 'time','data')


class DateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('id', 'room', 'type')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only': True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user