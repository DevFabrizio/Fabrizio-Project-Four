from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking, UserReservation
from .forms import BookingForm, UserReservationForm

# Create your views here.


class Home(generic.ListView):
    def get(self, request):
        return render(request, 'menu.html')


class Menu(View):
    def get(self, request):
        return render(request, 'menu.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')


class Maps(View):
    def get(self, request):
        return render(request, 'maps.html')


class ConfirmDelete(View):
    def get(self, request):
        return render(request, 'confirm_delete.html')


class EditReservation(View):
    def get(self, request, reservation_id):
        reservation = get_object_or_404(
            UserReservation,
            id=reservation_id,
            user=request.user)
        form = UserReservationForm(instance=reservation)
        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'edit_reservation.html', context)

    def post(self, request, reservation_id):

        reservation = get_object_or_404(
            UserReservation,
            id=reservation_id,
            user=request.user)
        
        form = UserReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('user_reservations')
        else:
            context = {
                'form': form,
                'reservation': reservation,
            }
            return render(request, 'edit_reservation.html', context)


class UserReservationsPage(View):
    
    def get(self, request):
        reservations = UserReservation.objects.filter(user=request.user)
        context = {
            'reservations': reservations,
        }
        return render(request, 'user_reservations.html', context)
    

class DeleteReservation(View):

    def post(self, request, reservation_id):
        if request.method == 'POST':
            reservation = UserReservation.objects.get(
                id=reservation_id, user=request.user)

            reservation.delete()
        return redirect('user_reservations')


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
        return render(request, 'user_booking.html', context)

    def post(self, request):
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
                form = UserReservationForm()
        context = {
            'form': form,
            'success_message': success_message,
            'reservation_name': reservation_name,
            }
        return render(request, 'user_booking.html', context)


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


