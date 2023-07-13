from django.contrib import admin
from .models import Booking, UserReservation


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    class to show the bookings made by users without the webiste account
    """
    list_filter = ('time_of_reservation',)
    list_display = ('reservation_name', 'time_of_reservation', 'num_of_guests')


@admin.register(UserReservation)
class UserReservationAdmin(admin.ModelAdmin):
    """
    class to show the bookings made by users with an account
    """
    list_filter = ('user', 'time_of_reservation')
    list_display = ('reservation_name',
                    'time_of_reservation',
                    'num_of_guests',
                    )
