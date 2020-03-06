from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import  LoginViewSet, RoomViewSet, DwellingViewSet, DeviceViewSet, SuggestionViewSet, ReadingViewSet, ProgressViewSet, userViewSet

router = routers.DefaultRouter()
router.register('room', LoginViewSet)
router.register('house', RoomViewSet)
router.register('Suggestion', DwellingViewSet)
router.register('users', SuggestionViewSet)
router.register('users', ReadingViewSet)
router.register('users', ProgressViewSet)
router.register('users', userViewSet)

urlpatterns = [
    path('', include(router.urls)),
]