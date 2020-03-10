from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import registrationView


router = routers.DefaultRouter()
router.register('auth/', registrationView)

urlpatterns = [
    path('', include(router.urls)),
]