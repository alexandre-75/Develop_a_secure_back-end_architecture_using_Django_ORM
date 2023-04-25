from django.contrib import admin
from .models import Client


@admin.register(Client)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display =["first_name", "last_name", "status_client", "email", "phone", "company", "sales_client"]