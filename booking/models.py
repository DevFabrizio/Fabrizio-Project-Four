from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """
    class to create the database model for booking
    made without an associated user
    """

    time_of_reservation = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    reservation_name = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_name


class UserReservation(models.Model):
    """
    class to create a database model which includes the user.
    The user database model is automatically created by the
    django.allauth library which provides also the login/logout
    and signup forms
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_reservation = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    reservation_name = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_name
