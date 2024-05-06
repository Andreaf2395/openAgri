from django.contrib import admin
from core.models import Device,QgisData,MobileData,WeatherData

admin.site.register(Device)
admin.site.register(MobileData)
admin.site.register(QgisData)
admin.site.register(WeatherData)
