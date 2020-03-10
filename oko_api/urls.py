
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from account.views import registrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dwelling/', include('Dwelling.urls')),
    path('register/', registrationView),
    #path('reg/', include('account.urls'))

]
