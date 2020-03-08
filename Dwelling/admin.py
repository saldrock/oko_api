from django.contrib import admin
from .models import Dwelling, Room, Device, RoomData, Suggestion

admin.site.register(Dwelling)
admin.site.register(Room)
admin.site.register(Device)
admin.site.register(RoomData)
admin.site.register(Suggestion)
