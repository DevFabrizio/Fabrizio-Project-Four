from django.forms import ModelForm
from .models import Booking, UserReservation
from django.forms.widgets import DateTimeInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'time_of_reservation': DateTimeInput(attrs={
                'type': 'datetime-local'})
        }


class UserReservationForm(ModelForm):
    class Meta:
        model = UserReservation
        fields = '__all__'
        widgets = {
            'time_of_reservation': DateTimeInput(attrs={
                'type': 'datetime-local'})
        }
