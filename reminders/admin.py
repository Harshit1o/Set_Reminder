from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'reminder_date', 'reminder_time', 'reminder_type', 'is_sent')
    list_filter = ('reminder_type', 'is_sent', 'reminder_date')
    search_fields = ('title', 'message', 'recipient')
    date_hierarchy = 'reminder_date'
