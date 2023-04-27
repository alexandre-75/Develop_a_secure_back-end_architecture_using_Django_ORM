from rest_framework import permissions


class IsManagementUser(permissions.BasePermission):
    """
    Permission customized to allow access only to users with the 'Management' role.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'MANAGEMENT':
            return request.method in ["GET", "POST", "PUT", "DELETE"]
        else:
            return False
