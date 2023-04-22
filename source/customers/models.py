from django.conf import settings
from django.db import models


class Client(models.Model):
    
    choice_status = [('POTENTIAL', 'POTENTIAL'),('EXISTING', 'EXISTING'),]
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    
    status_client = models.CharField(max_length=64, choices=choice_status)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    sales_client = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='sales_client')
    
    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
            return (
                f"{self.first_name} {self.last_name} | status : {self.status_client} "
                f"({self.company}) - Sales contact : {self.sales_contact}"
            )