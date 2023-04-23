from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import CustomersListSerializer, CustomersDetailSerializer
from .models import Client


class CustomersList(ListAPIView, CreateAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersListSerializer


class CustomersDetail(RetrieveAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersDetailSerializer
    
