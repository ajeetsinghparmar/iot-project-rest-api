from django.db import models
from datetime import datetime

class Place(models.Model):
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place

class Temperature(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=5)
    date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.place.place} on {self.date}'

class Humidity(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=5)
    date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.place.place} on {self.date}'

class Pressure(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=5)
    date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.place.place} on {self.date}'
