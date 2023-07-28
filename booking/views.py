# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm, UserReservationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
MAX_CAPACITY = 100


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


class ConfirmDelete(LoginRequiredMixin, View):
    """
    view that directs to the confirmation of deletion page.
    the get method retrieves the correct
    reservation to delete through the reservation id.
    the post method deletes that reservation when confirmed by the user
    """

    def get(self, request, reservation_id):

        reservation = get_object_or_404(
            Booking,
            id=reservation_id,)
        form = BookingForm(instance=reservation)

        if request.user.is_superuser:
            reservation = get_object_or_404(
                Booking,
                id=reservation_id)
            form = BookingForm(instance=reservation)

        elif request.user != reservation.user:
            return redirect('user_reservations')

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


class EditReservation(LoginRequiredMixin, View):
    """
    view to direct to the edit reservation page
    the get method restrieves the selected res through the id
    the post method resubmites the reservation after the user has edited it
    """
    # def test_func(self):
    #     return self.request.user.is_superuser

    def get(self, request, reservation_id):
        reservation = get_object_or_404(
            Booking,
            id=reservation_id)
        form = BookingForm(instance=reservation)

        """
        This if statement allows the users to only access and modify
        their own reservations and the superuser to modify all reservations
        """
        if request.user.is_superuser:
            reservation = get_object_or_404(
                Booking,
                id=reservation_id)
            form = BookingForm(instance=reservation)

        elif request.user != reservation.user:
            return redirect('user_reservations')

        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'edit_reservation.html', context)

    def post(self, request, reservation_id):

        reservation = get_object_or_404(
            Booking,
            id=reservation_id)

        form = BookingForm(request.POST, instance=reservation)

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
        reservations = Booking.objects.filter(user=request.user)
        all_res = Booking.objects.all()
        context = {
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
        success_message = ""
        if request.method == 'POST':
            form = UserReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.user = request.user
                """
                the "reservation.user var self assigns the user
                to the form based on the logged-in user
                """
                try:
                    reservation.clean()  # runs the clean method from the model
                except ValidationError as e:
                    form.add_error(None, str(e))  # Add the error to the form
                else:
                    success_message = """
                        Your reservation has been submitted correctly
                        """
                    reservation.save()
                    form = UserReservationForm()
            else:
                success_message = "THIS TIME AND DATE IS FULLY BOOKED!"

        context = {
            'form': form,
            'success_message': success_message,
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
        success_message = ""

        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)

                try:
                    reservation.clean()  # runs the clean method from the model
                except ValidationError as e:
                    form.add_error(None, str(e))  # Add the error to the form
                else:
                    success_message = """
                        Your reservation has been submitted correctly
                        """
                    reservation.save()
                    form = BookingForm()
            else:
                success_message = "THIS TIME AND DATE IS FULLY BOOKED!"

        context = {'form': form, 'success_message': success_message}
        return render(request, 'booking.html', context)
