from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    list_display = ["first_name", "last_name", "is_superuser", "role", "email"]
    list_per_page = 5
    ordering = ["last_name"]
    list_filter = ["role"]
    search_fields = ["first_name", "last_name", "role", "email"]