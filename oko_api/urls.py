
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#The API urls root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dwelling/', include('Dwelling.urls')),
    path('account/', include('account.urls'))

]
