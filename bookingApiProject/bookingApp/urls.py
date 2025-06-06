from django.urls import path

from .views import FitnessClassListAPI, FitnessClassDetailsAPI, BookingSlotDetailsAPI, BookingByEmailAPI

urlpatterns = [
    
    path('sessions-list', FitnessClassListAPI.as_view(), name='session-list'),
    
    path('sessions-list/session-details/<int:pk>', FitnessClassDetailsAPI.as_view(), name='session-details'),
    
    path('sessions-list/session-details/<int:pk>/bookings', BookingSlotDetailsAPI.as_view(), name='bookings'),
    
    path('bookings-by-email', BookingByEmailAPI.as_view(), name='bookings-by-email'),
]

