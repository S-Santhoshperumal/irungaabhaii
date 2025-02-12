# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from datetime import date, datetime, timedelta
from rest_framework.parsers import MultiPartParser, FormParser

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser, FormParser)



class AvailabilityViewset(viewsets.ModelViewSet):
     queryset = Availability.objects.all()
     serializer_class = AvailabilitySerializer

class ContactViewset(viewsets.ModelViewSet):
     queryset = Contact.objects.all()
     serializer_class = ContactSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
  

    def create(self, request, *args, **kwargs):
        car_id = request.data.get('car')
        pickup_date = request.data.get('pickup_date')
        return_date = request.data.get('return_date')

        car = Car.objects.get(pk=car_id)

        # Convert dates from strings to date objects if necessary
        pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d').date()
        return_date = datetime.strptime(return_date, '%Y-%m-%d').date()

        # Check for overlapping bookings within the selected dates
        overlapping_bookings = Booking.objects.filter(
            car=car,
            status='active',
            pickup_date__lt=return_date + timedelta(days=1),  # Bookings that start before the day after the return date
            return_date__gt=pickup_date - timedelta(days=1)  # Bookings that end after the day before the pickup date
        )

        if overlapping_bookings.exists():
            return Response({"error": "Car is already booked for the selected dates"}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with booking creation
        response = super().create(request, *args, **kwargs)

        # Update or create the availability entry for the booked dates
        Availability.objects.create(
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            available_quantity=0
        )

        return response

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if 'status' in request.data and request.data['status'] == 'canceled':
            car = instance.car

            # Check if there are any other active bookings for the same car
            active_bookings = Booking.objects.filter(
                car=car,
                status='active',
                pickup_date__lt=instance.return_date + timedelta(days=1),
                return_date__gt=instance.pickup_date - timedelta(days=1)
            )

            # If no other active bookings, mark the car as available
            if not active_bookings.exists():
                car.is_available = True
                car.save()

            # Update the availability record
            availability_record, created = Availability.objects.get_or_create(
                car=car,
                pickup_date=instance.pickup_date,
                return_date=instance.return_date,
            )
            if not created:
                availability_record.available_quantity = 1
                availability_record.save()

        return Response(serializer.data)
    

class CancellationViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer


    def create(self, request, *args, **kwargs):
        booking_id = request.data.get('booking')

        # Validate booking existence and status
        try:
            booking = Booking.objects.get(pk=booking_id, status='active')
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found or already canceled"}, status=status.HTTP_404_NOT_FOUND)

        # Proceed with the cancellation record creation
        response = super().create(request, *args, **kwargs)

        # Update the booking status to 'canceled'
        booking.status = 'canceled'
        booking.save()

        # Set the car's availability to 'True' (available)
        car = booking.car
        car.is_available = True
        car.save()

        # Update the availability record (or create if not exists)
        availability_record, created = Availability.objects.get_or_create(
            car=car,
            pickup_date=booking.pickup_date,
            return_date=booking.return_date,
        )

        if not created:
            # If record exists, update available quantity
            availability_record.available_quantity = 1
            availability_record.save()

        return response


from django.db.utils import IntegrityError
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        car_id = request.data.get('car')
        pickup_date = request.data.get('pickup_date')
        return_date = request.data.get('return_date')

        # Validate car existence
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

        # Convert dates from strings to date objects
        try:
            pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d').date()
            return_date = datetime.strptime(return_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure pickup_date is before return_date
        if pickup_date >= return_date:
            return Response({'error': 'Pickup date must be before return date.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for overlapping reservations
        if Reservation.objects.filter(
            car=car,
            pickup_date__lt=return_date + timedelta(days=1),
            return_date__gt=pickup_date - timedelta(days=1)
        ).exists():
            return Response({"error": "Car is already reserved for the selected dates"}, status=status.HTTP_400_BAD_REQUEST)

        # Check for overlapping bookings
        if Booking.objects.filter(
            car=car,
            status='active',
            pickup_date__lt=return_date + timedelta(days=1),
            return_date__gt=pickup_date - timedelta(days=1)
        ).exists():
            return Response({"error": "Car is already booked for the selected dates"}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with reservation creation
        try:
            reservation = Reservation.objects.create(
                user=request.user,
                car=car,
                reservation_date=date.today(),
                pickup_date=pickup_date,
                return_date=return_date
            )

            # Create or update availability record
            availability_record, created = Availability.objects.get_or_create(
                car=car,
                pickup_date=pickup_date,
                return_date=return_date,
                defaults={'available_quantity': 1}  # Default to 1 if newly created
            )

            if not created:
                # Reduce available quantity if already exists
                if availability_record.available_quantity > 0:
                    availability_record.available_quantity -= 1
                else:
                    return Response({'message': 'Car is successfully reserved!'}, status=status.HTTP_201_CREATED)
                    
            else:
                # If new, mark the car as unavailable
                availability_record.available_quantity = 0

              # Save updated availability data

        except IntegrityError:
            return Response({'message': 'Car is successfully reserved!'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Car is successfully reserved!', 'reservation_id': reservation.id}, status=status.HTTP_201_CREATED)