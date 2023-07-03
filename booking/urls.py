from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu.html/', views.Menu.as_view(), name='menu'),
    path('signup.html/', views.Signup.as_view(), name='signup'),
    path('booking.html/', views.BookingView.as_view(), name='booking'),
    path('user_booking.html/', views.UserReservations.as_view(),
         name='user_booking'),
    path('user_reservations.html/', views.UserReservationsPage.as_view(),
         name='user_reservations'),  
    path('user_reservations.html/<int:reservation_id>/delete/',
         views.DeleteReservation.as_view(), name='delete_reservation'),


]
