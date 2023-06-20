from django.contrib import admin
from .models import Customer, Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('reservation_name', 'time_of_reservation')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')





