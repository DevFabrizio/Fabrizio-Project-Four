from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking, Customer

# Create your views here.


class Home(generic.ListView):
    model = Booking
    template_name = 'base.html'


class Menu(View):
    def get(self, request):
        return render(request, 'menu.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')


class Booking(View):
    def get(self, request):
        return render(request, 'booking.html')