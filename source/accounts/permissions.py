from rest_framework import permissions


class IsManagementUser(permissions.BasePermission):
    """
    Permission customized to allow access only to users with the 'Management' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'MANAGEMENT'
