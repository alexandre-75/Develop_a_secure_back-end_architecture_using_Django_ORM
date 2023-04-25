from django.contrib import admin
from .models import Contract



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    
    list_display = ["id", "client_contract", "contract_status", "payment_due", "amount", "sales_contract"]
    list_per_page = 5
    ordering = ["-date_created"]
    list_filter = ["contract_status"]