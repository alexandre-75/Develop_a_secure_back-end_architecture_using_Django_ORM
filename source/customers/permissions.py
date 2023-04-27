from rest_framework import permissions
from django.db import connection

class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view): 
 
        user_id = request.user.id
        group_name = None
        
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT auth_group.name
                FROM auth_group
                INNER JOIN accounts_user_groups
                ON auth_group.id = accounts_user_groups.group_id
                WHERE accounts_user_groups.user_id = %s
                """,[user_id]
                )
            results = cursor.fetchall()

        for row in results:
            group_name = row[0]
            
        if group_name == "SALES_TEAM":
            return request.method in ["GET", "POST", "PUT"]
        elif group_name == "SUPPORT_TEAM":
            return request.method in ["GET"]
        else:
            return request.method in ["GET", "POST", "PUT", "DELETE"]
