from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.


class Booking(models.Model):
    """
    class to create the database model for booking
    made without an associated user
    """

    def clean(self):
        """
        This method checks if the restaurant is fully
        booked for a given time and date
        """
        if self.time_of_reservation and self.num_of_guests:
            existing_bookings = Booking.objects.filter(
                time_of_reservation=self.time_of_reservation
            )

            total_guests = sum(
                booking.num_of_guests for booking in existing_bookings
                )

            total_guests += self.num_of_guests

            if total_guests > 100:
                raise ValidationError("The restaurant is fully booked for"
                                      "your reservation time and date."
                                      "Try a new date or a new time.")

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True, blank=True)
    time_of_reservation = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    reservation_name = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_name
