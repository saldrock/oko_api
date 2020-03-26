from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DwellingViewSet,RoomViewSet, DataViewSet, DeviceViewSet,SuggestionViewSet

router = routers.DefaultRouter()
router.register('house', DwellingViewSet)
router.register('room', RoomViewSet)
router.register('device', DeviceViewSet)
router.register('data', DataViewSet)
router.register('suggestion', SuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
