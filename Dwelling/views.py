from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import Dwelling, Room, Device, RoomData, Suggestion
from .serializers import (
    DwellingSerializer,
    RoomSerializer,
    DeviceSerializer,
    DataSerializer,
    SuggestionSerializer,
)
from rest_framework.authentication import TokenAuthentication

class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer
    permission_classes = (IsAuthenticated,)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)


class DataViewSet(viewsets.ModelViewSet):
    queryset = RoomData.objects.all()
    serializer_class = DataSerializer
    permission_classes = (IsAuthenticated,)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)


class DwellingViewSet(viewsets.ModelViewSet):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer
    permission_classes = (AllowAny,)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsAuthenticated,)
