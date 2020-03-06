from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from data_vis.serializers import UserSerializer
#from .models import Room, Login, Dwelling
from .serializers import LoginSerializer, RoomSerializer, DwellingSerializer, DeviceSerializer, SuggestionSerializer,ReadingSerializer, ProgressSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)

class DwellingViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DwellingSerializer
    permission_classes = (AllowAny,)

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (AllowAny,)

class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SuggestionSerializer
    permission_classes = (AllowAny,)

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (AllowAny,)

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = (AllowAny,)

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)