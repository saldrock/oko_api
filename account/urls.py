from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    registration_view,
)
from rest_framework.authtoken.views import obtain_auth_token


app_name = "account"


urlpatterns = [
    path('register',registration_view, name="register"),
    path('login',obtain_auth_token, name="login"),
]