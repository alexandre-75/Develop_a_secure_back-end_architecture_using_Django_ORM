from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CustomersSerializer
from .models import Client


class CustomersList(ListAPIView, CreateAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersSerializer
    
