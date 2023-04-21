from django.conf import settings
from django.db import models


class Contrat(models.Model):

    choice_status = [('open', 'OPEN'),('signed', 'SIGNED'),]

    amount = models.FloatField(blank=True)
    payment_due =  models.DateField(null=True)

    contract_status = models.CharField(max_length=64, choices=choice_status)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    client = models.ForeignKey(to=Client, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return f"Contrat num. {self.id} | Client: {self.client.first_name} | Sales Contact: {self.sales_contact}"