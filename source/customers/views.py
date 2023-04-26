from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomersListSerializer, CustomersDetailSerializer
from .models import Client


class CustomersList(ListAPIView, CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = CustomersListSerializer


class CustomersDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = CustomersDetailSerializer
    
