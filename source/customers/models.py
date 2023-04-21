from django.conf import settings
from django.db import models


class Client(models.Model):
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
            return (
                f"{self.first_name} {self.last_name} "
                f"({self.company}) - Sales contact : {self.sales_contact}"
            )