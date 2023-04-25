from django.contrib import admin
from .models import Client


@admin.register(Client)
class CustomerAdmin(admin.ModelAdmin):
    
    list_display =["first_name", "last_name", "status_client", "email", "phone", "company", "sales_client"]
    search_fields = ["first_name", "last_name", "email", "status_client"]
    list_filter = ["status_client"]
    list_per_page = 5
    ordering = ["last_name"]
