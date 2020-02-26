from django.contrib import admin
from .models import Room, House, Control, Suggestion, Devices

admin.site.register(Room)
admin.site.register(House)
admin.site.register(Control)
admin.site.register(Suggestion)
admin.site.register(Devices)
