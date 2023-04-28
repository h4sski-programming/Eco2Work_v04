from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    ACTIVITY_VEHICLE_CHOICES = [
        ('foot', 'foot'),
        ('bike', 'bike'),
        ('scooter', 'scooter'),
        ]

    __tablename__ = 'activity'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=0)
    distance = models.PositiveIntegerField()
    vehicle = models.CharField(
        max_length=100,
        choices=ACTIVITY_VEHICLE_CHOICES,
        default=ACTIVITY_VEHICLE_CHOICES[1][0]
        )
    date = models.DateField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.distance}km {self.date}'
