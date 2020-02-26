from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RoomViewSet, TimeViewSet, DataViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('room', RoomViewSet)
router.register('data_type', DataViewSet)
router.register('time', TimeViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]