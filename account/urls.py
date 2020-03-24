from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    registration_view,
)


app_name = "account"


urlpatterns = [
    path('register',registration_view, name="register"),
]