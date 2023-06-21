from django.contrib import admin
from .models import Customer, Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('reservation_name', 'time_of_reservation')
    list_display = ('reservation_name', 'time_of_reservation', 'num_of_guests')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')





