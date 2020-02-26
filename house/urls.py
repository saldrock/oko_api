from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import  UserViewSet, RoomViewSet, HouseViewSet, SuggestionViewSet

router = routers.DefaultRouter()
router.register('room', RoomViewSet)
router.register('house', HouseViewSet)
router.register('Suggestion', SuggestionViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]