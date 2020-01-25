from django.contrib import admin
from .models import Room, TimePeriod, DataType

admin.site.register(Room)
admin.site.register(TimePeriod)
admin.site.register(DataType)

