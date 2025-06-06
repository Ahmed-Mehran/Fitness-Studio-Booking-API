from django.contrib import admin
from .models import FitnessClassSession, BookingSlot


admin.site.register(FitnessClassSession)  # register the FitnessClassSession on Admin Dashboard
admin.site.register(BookingSlot)