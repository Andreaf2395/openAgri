from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    macaddress=models.CharField(max_length=100)
    type=models.IntegerField(null=True)

    users= models.ManyToManyField(User)
    def __str__(self):
        return self.name
    
   


class MobileData(models.Model):
    geo_location_lat = models.FloatField(null=True)
    geo_location_long = models.FloatField(null=True)
    image_path=models.CharField(max_length=256)
    qr_code=models.TextField()
    recording_time=models.DateTimeField(null=True)

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )


class QgisData(models.Model):
    geo_location_lat = models.FloatField(null=True)
    geo_location_long = models.FloatField(null=True)
    ndvi = models.FloatField(null=True)
    gndvi =models.FloatField(null=True)
    lai =models.FloatField(null=True)
    msdvi=models.FloatField(null=True)
    recording_time=models.DateTimeField()
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )

class WeatherData(models.Model):
    geo_location_lat = models.FloatField(null=True)
    geo_location_long = models.FloatField(null=True)
    wind_direction=models.CharField(max_length=128,null=True)
    wind_speed=models.CharField(max_length=128,null=True)
    rainfall=models.CharField(max_length=128,null=True)
    sunshine= models.CharField(max_length=128,null=True)
    temperature= models.CharField(max_length=128,null=True)
    humidity= models.CharField(max_length=128,null=True)
    recording_time=models.DateTimeField()
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )