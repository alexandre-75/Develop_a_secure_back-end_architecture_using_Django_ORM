from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    list_display = ["event_name", "event_status", "client_events", "contract_events", "sales_events", "support_events"]
    list_per_page = 5
    ordering = ["date_created"]
    list_filter = ["event_status"]
    fieldsets = (
        ("Event Informations", {
            "fields": (
                "event_name",
                "event_status",
                "event_date",
                "event_notes",
                "attendees",  
            ),
        }),
        ("Additional Information", {
            "fields": (
                "client_events",
                "contract_events",
                "sales_events",
                "support_events",
            )})
    )
    