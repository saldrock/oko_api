from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

import account
from .views import (
    registration_view,
   # AccountViewSet,
    account_view,
    User_DataViewSet,

)

app_name = "account"
router = routers.DefaultRouter()
router.register('users',account_view)

urlpatterns = [
    # path('register',registration_view, name="register"),
    # path('login',obtain_auth_token, name="login"),
    # path('user',account_view, name='userlist'),
    path('', include(router.urls)),
]

