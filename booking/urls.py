from . import views
from django.urls import path

"""
list of url path to allow the user to browse trhough the pages and
to pass the relevant ids for the edit and delete functions of the database
"""

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu.html/', views.Menu.as_view(), name='menu'),
    path('signup.html/', views.Signup.as_view(), name='signup'),
    path('maps.html/', views.Maps.as_view(), name='maps'),
    path('booking.html/', views.BookingView.as_view(), name='booking'),
    path('confirm_delete.html/<int:reservation_id>/',
         views.ConfirmDelete.as_view(),
         name='confirm_delete'),
    path('user_booking.html/', views.UserReservations.as_view(),
         name='user_booking'),
    path('user_reservations.html/', views.UserReservationsPage.as_view(),
         name='user_reservations'),
    path('edit_reservation.html/<int:reservation_id>/',
         views.EditReservation.as_view(),
         name='edit_reservation'),


]
