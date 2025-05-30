from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'title', 'message', 'reminder_date', 'reminder_time', 
                  'reminder_type', 'recipient', 'created_at', 'is_sent']
        read_only_fields = ['id', 'created_at']
