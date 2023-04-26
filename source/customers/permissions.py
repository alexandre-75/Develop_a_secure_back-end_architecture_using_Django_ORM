from rest_framework import permissions
from .models import Client


class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view):  
        
        if request.user.role == "SALE":
            return request.method in ["GET", "POST", "PUT"]
        elif request.user.role == "SUPPORT":
            return request.method in ["GET"]
        else:
            return request.method in ["GET", "POST", "PUT", "DELETE"]
