from django.contrib import admin
from .models import Place, Temperature, Humidity, Pressure

admin.site.register(Place)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Pressure)
