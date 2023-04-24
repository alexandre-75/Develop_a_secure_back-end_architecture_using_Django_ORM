from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import CustomersListSerializer, CustomersDetailSerializer
from .models import Client


class CustomersList(ListAPIView, CreateAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersListSerializer


class CustomersDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersDetailSerializer
    
