from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404

from .models import FitnessClassSession, BookingSlot
from .serializers import FitnessClassSessionSerializer, BookingSlotSerializer


class FitnessClassListAPI(APIView):
    
    def get(self, request):
        
        all_fitness_sessions = FitnessClassSession.objects.all()
        
        serializer = FitnessClassSessionSerializer(all_fitness_sessions, many=True)
        
        return Response(serializer.data)


class FitnessClassDetailsAPI(APIView):
    
    def get(self, request, pk):
        
        fitness_session = FitnessClassSession.objects.get(pk=pk)
        
        serializer = FitnessClassSessionSerializer(fitness_session)
        
        return Response(serializer.data)
    
    
class BookingSlotDetailsAPI(APIView):
    
    def get(self, request, pk):

        booking_slot = BookingSlot.objects.filter(session_id=pk)
        
        serializer = BookingSlotSerializer(booking_slot, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, pk):
        
        curr_session_obj = get_object_or_404(FitnessClassSession, pk=pk)

        ## CHECK IF THERE ARE ANY AVAILABLE SLOTS FOR CURRENT SESSION OBJECT
        if curr_session_obj.total_slots <= 0:
            return Response({"error": "No available slots for this session."}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = BookingSlotSerializer(data=request.data)
        
        if serializer.is_valid():
            client_email = serializer.validated_data['client_email']
            
            ## CHECK FOR, IF A USER HAS ALREADY BOOKED A SPECIFIC SESSION WITH A SAME EMAIL AND IF HE TRIES TO AGAIN BOOK IT, WILL RECEIVE ERROR
            if BookingSlot.objects.filter(session=curr_session_obj, client_email=client_email).exists():       
                return Response({"error": "You have already booked this session."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save(session=curr_session_obj)
            
            curr_session_obj.total_slots -= 1
            curr_session_obj.save(update_fields=['total_slots'])
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
class BookingByEmailAPI(APIView):
    
    def get(self, request):
        email = request.query_params.get('email')

        ## If we have not provided any email in the query
        if not email:
            return Response({"error": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        ## If the email provided as part of query does not even exist in the BookSlot database
        if not(BookingSlot.objects.filter(client_email=email).exists()):
            return Response({"error": "No Bookings By This Email"}, status=status.HTTP_400_BAD_REQUEST)
        
        bookings = BookingSlot.objects.filter(client_email=email)
        
        serializer = BookingSlotSerializer(bookings, many=True)
        
        return Response(serializer.data)
        
            
        
        
            
            
        
    
    
