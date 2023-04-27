from rest_framework import permissions
from .models import Event


class EventPermissions(permissions.BasePermission):

    def has_permission(self, request, view):  
        
        if request.user.role == "SALE":
            return request.method in ["GET", "POST"]
        elif request.user.role == "SUPPORT":
            return request.method in ["GET", "PUT"]
        else:
            return request.method in ["GET", "POST", "PUT", "DELETE"]
        