from rest_framework.generics import ListAPIView
from .serializers import CustomersSerializer
from .models import Client


class CustomersList(ListAPIView):
    
    queryset = Client.objects.all()
    serializer_class = CustomersSerializer
    
