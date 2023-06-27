from django.forms import ModelForm
from .models import Booking
from django.forms.widgets import DateTimeInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'time_of_reservation': DateTimeInput(attrs={'type': 'datetime-local'})
        }