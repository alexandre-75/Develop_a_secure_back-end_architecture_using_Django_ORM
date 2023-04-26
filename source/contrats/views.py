from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer, ContractDetailSerializer
from .models import Contract
from rest_framework.permissions import IsAuthenticated


class ContractList(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer


class ContractDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer