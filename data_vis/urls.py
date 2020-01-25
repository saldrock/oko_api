from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RoomViewSet, TimeViewSet, DataViewSet


router = routers.DefaultRouter()
router.register('room', RoomViewSet)
router.register('data_type', DataViewSet)
router.register('time', TimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]