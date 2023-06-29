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
    """
    meta class includes the widget to easily allow the users to pick a
    date and time, the exclude clause cuts off the user from the form as
    to allow the form to automatically generate the user based on who is 
    logged in at the moment.
    """

    class Meta:
        model = UserReservation
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'time_of_reservation': DateTimeInput(attrs={
                'type': 'datetime-local'})
        }