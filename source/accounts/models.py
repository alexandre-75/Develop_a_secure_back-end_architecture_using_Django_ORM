from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    class Role(models.TextChoices):
        MANAGEMENT = ("MANAGEMENT", "Management")
        SALE = ("SALE", "Sales")
        SUPPORT = ("SUPPORT", "Support")
    
    username = models.CharField (max_length=50, unique=True)
    email = models.EmailField(unique=True)
    
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    role = models.CharField(max_length=25, choices=Role.choices, verbose_name='role')

    def is_management(self):
        return self.groups.filter(name="Management").exists()

    def is_sale(self):
        return self.groups.filter(name="Sale").exists()

    def is_support(self):
        return self.groups.filter(name="Support").exists()
