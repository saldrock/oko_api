from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
   account_view,
)

# Account URLs
app_name = "account"
router = routers.DefaultRouter()
router.register('users',account_view)

urlpatterns = [
    path('', include(router.urls)),
]

