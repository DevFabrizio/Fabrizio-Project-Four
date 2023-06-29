from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking, UserReservation
from .forms import BookingForm, UserReservationForm

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


class UserReservations(View):

    def get(self, request):
        form = UserReservationForm()

        context = {
            'form': form,
            'reservation_name': form['reservation_name'],
            'time_of_reservation': form['time_of_reservation'],
            'num_of_guests': form['num_of_guests'],
            'allergies': form['allergies'],
            'kids_under_10': form['kids_under_10'],
            }
        return render(request, 'user_reservations.html', context)

    def post(self, request):
        all_reservations = UserReservation.objects.filter(user=request.user)
        success_message = """
            Your reservation has been submitted correctly
            """
        reservation_name = ""
        if request.method == 'POST':
            form = UserReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                """
                the "reservation.user var self assigns the user
                to the form based on the logged-in user
                """
                reservation.user = request.user
                reservation.save()
                reservation_name = form.cleaned_data['reservation_name']
                form = UserReservationForm()
        context = {
            'form': form,
            'success_message': success_message,
            'reservation_name': reservation_name,
            'all_reservations': all_reservations
            }
        return render(request, 'user_reservations.html', context)


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
                form = BookingForm()
        context = {'form': form, 'success_message': success_message}
        return render(request, 'booking.html', context)
