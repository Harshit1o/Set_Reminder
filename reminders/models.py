from django.db import models

# Create your models here.
class Reminder(models.Model):
    REMINDER_TYPE_CHOICES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
    ]
    
    title = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPE_CHOICES, default='EMAIL')
    recipient = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Reminder: {self.title or self.message[:20]+'...'} on {self.reminder_date} at {self.reminder_time}"
