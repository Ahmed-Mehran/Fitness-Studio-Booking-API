from rest_framework import serializers
from .models import FitnessClassSession, BookingSlot


class BookingSlotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookingSlot
        fields= '__all__'

class FitnessClassSessionSerializer(serializers.ModelSerializer):
    
    bookings = BookingSlotSerializer(many=True, read_only=True)
    
    class Meta:
        model = FitnessClassSession
        fields= '__all__'
        
        
