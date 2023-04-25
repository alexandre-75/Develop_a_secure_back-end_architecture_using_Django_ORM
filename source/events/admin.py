from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    list_display = ["event_name", "event_status", "client_events", "contract_events", "sales_events", "support_events"]