from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):

    time_of_reservation = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    reservation_name = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_name


class UserReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_reservation = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    reservation_name = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_name
