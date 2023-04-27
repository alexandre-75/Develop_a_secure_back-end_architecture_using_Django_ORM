from django.contrib import admin
from .models import Client
from events.models import Event


@admin.register(Client)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display =["first_name", "last_name", "status_client", "email", "phone", "company", "sales_client"]
    search_fields = ["first_name", "last_name", "email", "status_client"]
    list_filter = ["status_client"]
    list_per_page = 5
    ordering = ["last_name"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user
        if user.groups.filter(name="SALES_TEAM").exists():
            queryset = queryset.filter(sales_client_id=user)
        elif user.groups.filter(name="SUPPORT_TEAM").exists():
            user_events = Event.objects.filter(support_events_id=user)
            client_ids = user_events.values_list('client_events_id', flat=True)
            queryset = queryset.filter(id__in=client_ids)
        return queryset