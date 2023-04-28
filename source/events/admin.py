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
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user
        if user.groups.filter(name="SALES_TEAM").exists():
            queryset = queryset.filter(sales_events_id=user)
        elif user.groups.filter(name="SUPPORT_TEAM").exists():
            queryset = Event.objects.filter(support_events_id=user)
        return queryset