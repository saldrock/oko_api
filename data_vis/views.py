from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Room, DataType, TimePeriod
from .serializers import RoomSerializer, TimePeriodSerializer, DateTypeSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def add_time(self, request, pk):
        response = {'message': 'its working'}
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = {'you cant do that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'you cant create like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TimeViewSet(viewsets.ModelViewSet):
    queryset = TimePeriod.objects.all()
    serializer_class = TimePeriodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DataViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DateTypeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
