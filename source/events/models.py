from django.db import models
from customers.models import Client


class Event(models.Model):
    
    choice_status = [('open', 'OPEN'),('close', 'CLOSED'),]
    
    event_name = models.CharField(max_length=1024)
    event_date = models.DateTimeField()
    event_notes = models.TextField(null=True, blank=True)
    attendees = models.PositiveIntegerField()
    
    event_status = models.CharField(max_length=64, choices=choice_status)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    sales_contact = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    
    def __str__(self):
        return f"Event. {self.id} | Support Contact: {self.support_contact} | Event Status: {self.event_status}"
