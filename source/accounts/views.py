from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserListSerializer, UserDetailSerializer, SignupSerializer
from .models import User



class UserList(ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
    
class UserDetail(RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    
class SignupView(ListAPIView, CreateAPIView):

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

