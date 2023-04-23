from rest_framework.generics import ListAPIView
from .serializers import UserListSerializer, UserDetailSerializer
from .models import User


class UserList(ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    

