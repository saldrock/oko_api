from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Dwelling, Room, Device
from .serializers import DwellingSerializer, RoomSerializer, DeviceSerializer, DataSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = UserSerializer
#yeet
#kSFIHSDFD

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class DataViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DataSerializer
    permission_classes = (AllowAny,)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class DwellingViewSet(viewsets.ModelViewSet):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer
    permission_classes = (AllowAny,)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (AllowAny,)
