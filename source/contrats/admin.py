from django.contrib import admin
from .models import Contract
from events.models import Event



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    
    list_display = ["id", "client_contract", "contract_status", "payment_due", "amount", "sales_contract"]
    list_per_page = 5
    ordering = ["-date_created"]
    list_filter = ["contract_status"]
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user
        if user.groups.filter(name="SALES_TEAM").exists():
            queryset = queryset.filter(sales_contract_id=user)
        elif user.groups.filter(name="SUPPORT_TEAM").exists():
            user_events = Event.objects.filter(support_events_id=user)
            client_ids = user_events.values_list('contract_events_id', flat=True)
            queryset = queryset.filter(id__in=client_ids)
        return queryset