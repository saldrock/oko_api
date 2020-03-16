from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DwellingViewSet, RoomViewSet, DataViewSet, DeviceViewSet

router = routers.DefaultRouter()
router.register('house', DwellingViewSet)
router.register('room', RoomViewSet)
router.register('device', DeviceViewSet)
router.register('data', DataViewSet)
#router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
