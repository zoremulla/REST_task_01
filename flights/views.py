from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .serializers import FlightSerializer
from .serializers import UpcomingSerializer
from datetime import date





class Flightlist(ListAPIView):
    queryset=Flight.objects.all()
    serializer_class = FlightSerializer

class Upcoming_bookings(ListAPIView):
    queryset=Booking.objects.filter(date__gte=date.today())
    serializer_class = UpcomingSerializer
