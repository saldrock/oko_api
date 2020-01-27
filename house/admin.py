from django.contrib import admin
from .models import Room, House, Control, Suggestion

admin.site.register(Room)
admin.site.register(House)
admin.site.register(Control)
admin.site.register(Suggestion)