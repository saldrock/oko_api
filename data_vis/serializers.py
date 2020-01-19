from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Room
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    model = Room
    fields = ('id', 'name', 'period')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only': True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

