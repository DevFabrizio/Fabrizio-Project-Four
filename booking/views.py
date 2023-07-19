# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Booking, UserReservation
from .forms import BookingForm, UserReservationForm

# Create your views here.


class Home(generic.ListView):
    # view to direct to the home page
    def get(self, request):
        return render(request, 'menu.html')


class Menu(View):
    # view to direct to the menu page
    def get(self, request):
        return render(request, 'menu.html')


class Signup(View):
    # view to direct to the signup page, logic handled by django.allauth
    def get(self, request):
        return render(request, 'signup.html')


class Maps(View):
    # view to direct to the maps page
    def get(self, request):
        return render(request, 'maps.html')


class ConfirmDelete(View):
    """
    view that directs to the confirmation of deletion page.
    the get method retrieves the correct
    reservation to delete through the reservation id.
    the post method deletes that reservation when confirmed by the user
    """

    def get(self, request, reservation_id):
        # reservation = get_object_or_404(
        #     UserReservation,
        #     id=reservation_id,
        #     user=request.user)
        # form = UserReservationForm(instance=reservation)

        reservation = get_object_or_404(
            Booking,
            id=reservation_id,)
        form = BookingForm(instance=reservation)
        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'confirm_delete.html', context)

    def post(self, request, reservation_id):
        if request.method == 'POST':
            reservation = Booking.objects.get(
                id=reservation_id)
            reservation.delete()
        return redirect('user_reservations')


class EditReservation(View):
    """
    view to direct to the edit reservation page
    the get method restrieves the selected res through the id
    the post method resubmites the reservation after the user has edited it
    """
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
    """
        view to direct to the user reservation page,
        the get method retrieves
        all the reservations made by the logged in user
    """

    def get(self, request):
        reservations = UserReservation.objects.filter(user=request.user)
        all_res = Booking.objects.all()
        all_user_res = UserReservation.objects.all()
        context = {
            'all_user_res': all_user_res,
            'reservations': reservations,
            'all_res': all_res
        }
        return render(request, 'user_reservations.html', context)


class UserReservations(View):
    """
    view to create the reservation from a logged in user
    the get method displays all the fields that the user needs to fill,
    the post method submits the reservation to the database
    """

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
    """
    view to create the reservation for users without an account.
    the get method displays all the required fields.
    the post method saves the reservation to the database
    """
    def get(self, request):
        form = BookingForm()
        context = {
            'form': form,
            }
        return render(request, 'booking.html', context)

    def post(self, request):
        form = BookingForm()
        success_message = """
            Your reservation has been submitted correctly
            """

        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                form = BookingForm()
        context = {'form': form, 'success_message': success_message}
        return render(request, 'booking.html', context)
