from django.conf import settings
from django.db import models
from customers.models import Client


class Contract(models.Model):

    choice_status = [('open', 'OPEN'),('signed', 'SIGNED'),]

    amount = models.FloatField(blank=True)
    payment_due =  models.DateField(null=True)

    contract_status = models.CharField(max_length=64, choices=choice_status)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    client_contract = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL, related_name='client_contract')
    sales_contract = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name='sales_contract')
    
    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return (f"{self.id}")