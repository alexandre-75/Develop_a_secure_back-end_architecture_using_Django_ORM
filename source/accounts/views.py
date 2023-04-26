from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserListSerializer, UserDetailSerializer, SignupSerializer
from .models import User
from .permissions import IsManagementUser



class UserList(ListAPIView):
    
    permission_classes = [IsAuthenticated, IsManagementUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    
class UserDetail(RetrieveAPIView):
    
    permission_classes = [IsAuthenticated, IsManagementUser]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    
class SignupView(ListAPIView, CreateAPIView):

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

