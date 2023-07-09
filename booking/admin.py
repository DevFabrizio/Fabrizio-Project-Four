from django.contrib import admin
from .models import Booking, UserReservation


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('reservation_name', 'time_of_reservation')
    list_display = ('reservation_name', 'time_of_reservation', 'num_of_guests')


@admin.register(UserReservation)
class UserReservationAdmin(admin.ModelAdmin):
    list_filter = ('user', 'time_of_reservation')
    list_display = ('reservation_name',
                    'time_of_reservation',
                    'num_of_guests',
                    )







