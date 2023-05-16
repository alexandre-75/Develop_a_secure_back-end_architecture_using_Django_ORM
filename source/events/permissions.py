from rest_framework import permissions
from .models import Event
from contrats.models import Contract


class EventPermissions(permissions.BasePermission):

    def has_permission(self, request, view):  
        
        if request.user.role == "SALE":
            return request.method in ["GET", "POST"]
        elif request.user.role == "SUPPORT":
            return request.method in ["GET", "PUT"]
        else:
            return request.method in ["GET", "POST", "PUT", "DELETE"]
   

class ContratSignePermission(permissions.BasePermission):
    message = "The contract must be signed to create an event."

    def has_permission(self, request, view):
        if request.method == "POST":
            contrat_id = request.data.get("contract_events")
            print(contrat_id)
            if contrat_id:
                try:
                    contrat = Contract.objects.get(id=contrat_id)
                    if contrat.contract_status != "signed":
                        return False
                except Contract.DoesNotExist:
                    return False
        return True
