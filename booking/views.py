from django.shortcuts import render
from django.views import generic
from .models import Booking, Customer

# Create your views here.


class Booking(generic.ListView):
    model = Booking
    template_name = 'base.html'
