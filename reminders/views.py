from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    @swagger_auto_schema(
        operation_summary="List all reminders",
        operation_description="Returns a list of all reminders in the system."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new reminder",
        operation_description="Creates a new reminder with the provided information.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['message', 'reminder_date', 'reminder_time', 'reminder_type', 'recipient'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Optional reminder title'),
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Reminder message content'),
                'reminder_date': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Date for the reminder (YYYY-MM-DD)'),
                'reminder_time': openapi.Schema(type=openapi.TYPE_STRING, format='time', description='Time for the reminder (HH:MM:SS)'),
                'reminder_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['EMAIL', 'SMS'], description='How to send the reminder'),
                'recipient': openapi.Schema(type=openapi.TYPE_STRING, description='Email address or phone number'),
            }
        ),
        responses={201: ReminderSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a specific reminder",
        operation_description="Returns the details of a specific reminder."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a specific reminder",
        operation_description="Updates all fields of a specific reminder."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a specific reminder",
        operation_description="Updates one or more fields of a specific reminder."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a specific reminder",
        operation_description="Deletes a specific reminder from the system."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
