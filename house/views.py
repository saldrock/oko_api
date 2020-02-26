from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from data_vis.serializers import UserSerializer
from .models import Room, House, Control, Suggestion
from .serializers import RoomSerializer, HouseSerializer, SuggestionSerializer, ControlSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (AllowAny,)

class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SuggestionSerializer
    permission_classes = (AllowAny,)
