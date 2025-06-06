# Fitness-Studio-Booking-API
A Django REST Framework project that provides a simple backend system for managing fitness class sessions (Yoga, Zumba, HIIT) and user bookings. This project allows clients to view available sessions and book them, while ensuring proper validation and slot management.

## Features
-View all available fitness class sessions (GET /sessions-list)

-View details of a single session (GET /sessions-list/session-details/<pk>)

-View all bookings for a session (GET /sessions-list/session-details/<pk>/bookings)

-Book a slot in a session (POST /sessions-list/session-details/<pk>/bookings)

-Prevent overbooking and duplicate bookings by email

-Get all bookings made by a specific email (GET /bookings?email=example@example.com)

## Tech Stack
Backend: Django, Django REST Framework

Database: SQLite (default, can be changed to PostgreSQL)

Admin Panel: Used for adding fitness class sessions securely

## Models

__FitnessClassSession__

  class_name: Class type (Yoga, Zumba, HIIT)
  
  session_datetime: Date & Time of session (unique with class name)
  
  instructor: Instructor name
  
  total_slots: Number of slots available for booking

__BookingSlot__

  session: Foreign key to FitnessClassSession
  
  client_name: Name of the client
  
  client_email: Email of the client (used to identify unique bookings)
  
  Automatically decrements total_slots on valid booking


