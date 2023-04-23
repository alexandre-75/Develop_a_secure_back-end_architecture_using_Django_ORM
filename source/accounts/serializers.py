from rest_framework.serializers import ModelSerializer
from .models import User


class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "email",]
        
class UserDetailSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"