from django.db import models


class FitnessClassSession(models.Model):
    CLASS_CHOICES = [
        ('Yoga', 'Yoga'),
        ('Zumba', 'Zumba'),
        ('HIIT', 'HIIT'),
    ]

    class_name = models.CharField(max_length=50, choices=CLASS_CHOICES)
    
    session_datetime = models.DateTimeField()
    
    instructor = models.CharField(max_length=100)
    
    total_slots = models.IntegerField()

    class Meta:
        unique_together = ('class_name', 'session_datetime')  # Enforce uniqueness 

    def __str__(self):
        return f"{self.class_name} on {self.session_datetime}"
    


class BookingSlot(models.Model):
    
    session = models.ForeignKey('FitnessClassSession',  on_delete=models.CASCADE,related_name='bookings') # Link to the session being booked
    
    client_name = models.CharField(max_length=100)
    
    client_email = models.EmailField()

    def __str__(self):
        return f"{self.client_name} booked {self.session}"

    