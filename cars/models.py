from django.db import models
from user.models import User

class Car(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    fuel = models.CharField(max_length=50)
    seats = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)  # Store images in /media/cars/

    def __str__(self):
        return self.name

class Booking(models.Model):
     STATUS_CHOICES = [
        ('active', 'Active'),
        ('canceled', 'Canceled'),
     ]
     booking_id = models.AutoField(primary_key=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     car = models.ForeignKey(Car, on_delete=models.CASCADE)
     booking_date = models.DateField()
     pickup_date = models.DateField()
     return_date = models.DateField()
     total_price = models.FloatField()

     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

     def __str__(self):
        return f"Booking {self.booking_id} - {self.status}"

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    pickup_date = models.DateField()
    return_date = models.DateField()

class Cancellation(models.Model):
    cancellation_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cancellation_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Cancellation {self.cancellation_id} for Booking {self.booking.booking_id}"

class Availability(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
    pickup_date = models.DateField()
    return_date = models.DateField()
    available_quantity = models.IntegerField()