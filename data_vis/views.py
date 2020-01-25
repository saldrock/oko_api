from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Room, DataType, TimePeriod
from .serializers import RoomSerializer, TimePeriodSerializer, DateTypeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class TimeViewSet(viewsets.ModelViewSet):
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer
    permission_classes = (AllowAny,)


class DataViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DateTypeSerializer
    permission_classes = (AllowAny,)
