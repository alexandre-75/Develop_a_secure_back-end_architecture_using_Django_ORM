from rest_framework import permissions
from django.db import connection
from django.contrib.auth.models import Group

class ContractPermissions(permissions.BasePermission):
 
        def has_permission(self, request, view):
            user_groups = Group.objects.filter(user=request.user)
            group_names = ', '.join(user_groups.values_list('name', flat=True))
            print(group_names)

            if "SALES_TEAM" in group_names:
                return request.method in ["GET", "POST", "PUT"]
            elif "SUPPORT_TEAM" in group_names:
                return request.method in ["GET"]
            else:
                return request.method in ["GET", "POST", "PUT", "DELETE"]