from django.contrib import admin
from .models import Contract



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    
    list_display = ["id", "client_contract", "contract_status", "payment_due", "amount", "sales_contract"]