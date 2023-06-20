from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    time_of_res = models.DateTimeField(auto_now=False, auto_now_add=False)
    num_of_guests = models.IntegerField()
    kids_under_10 = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    res_name = models.CharField(max_length=20)

    def __str__(self):
        return self.res_name, self.time_of_res
