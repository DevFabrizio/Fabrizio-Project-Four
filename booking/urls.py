from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu.html/', views.Menu.as_view(), name='menu'),
    path('signup.html/', views.Signup.as_view(), name='signup'),
    path('booking.html/', views.BookingView.as_view(), name='booking'),
]
