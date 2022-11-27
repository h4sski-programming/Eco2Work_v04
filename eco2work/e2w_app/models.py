from django.db import models

from const import *

class Activity(models.Model):
    __tablename__ = 'activity'
    distance = models.IntegerField(max_length=3)
    vehicle = models.CharField(
        max_length=100,
        choices=ACTIVITY_VEHICLE_CHOICES,
        default=ACTIVITY_VEHICLE_CHOICES[1][0]
        )
    date = models.DateField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.distance} {self.vehicle} {self.date}'
