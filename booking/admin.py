from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    class to show the bookings made by users
    and visitors without the webiste account
    """
    list_filter = ('time_of_reservation',)
    list_display = ('id',
                    'reservation_name',
                    'time_of_reservation',
                    'num_of_guests')
