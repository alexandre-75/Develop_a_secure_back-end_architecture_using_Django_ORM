from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer, ContractDetailSerializer
from .models import Contract


class ContractList(ListAPIView):
    
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer


class ContractDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer