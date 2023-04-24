from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer
from .models import Contract


class ContractList(ListAPIView):
    
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer