
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_vis/', include('data_vis.urls')),
    path('auth/', obtain_auth_token),
    path('house/', include('house.urls')),
    #this is a test
]
