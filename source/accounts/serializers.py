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
        

class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
