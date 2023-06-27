from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm

# Create your views here.


class Home(generic.ListView):
    # template_name = 'base.html'
    def get(self, request):
        return render(request, 'menu.html')


class Menu(View):
    def get(self, request):
        return render(request, 'menu.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')


class BookingView(View):

    def get(self, request):
        form = BookingForm()
        context = {'form': form}
        return render(request, 'booking.html', context)

    def post(self, request):
        form = BookingForm()

        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = """
                    Your reservation has been submitted correctly
                    """
        context = {'form': form, 'success_message': success_message}
        return render(request, 'booking.html', context)
