from rest_framework import serializers
from .models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flight
        fields=['destination', 'time','price','id']


class UpcomingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['flight', 'date','id']

