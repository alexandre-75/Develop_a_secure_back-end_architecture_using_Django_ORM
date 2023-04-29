from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from .models import User


class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "username", "email",]

     
class UserDetailSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
