from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer, ContractDetailSerializer
from .models import Contract
from events.models import Event
from rest_framework.permissions import IsAuthenticated
from .permissions import ContractPermissions


def get_contracts_queryset(user):
    if user.role == "SALE":
        return Contract.objects.filter(sales_contract_id=user.id)
    elif user.role == "SUPPORT":
        list_events = Event.objects.filter(support_events=user.id)
        list_contracts = [event.contract_events_id for event in list_events]
        return Contract.objects.filter(id__in=list_contracts)
    else:
        return Contract.objects.all()


class ContractList(ListAPIView):
    
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractListSerializer
    
    def get_queryset(self):
        user = self.request.user
        return get_contracts_queryset(user)
        

class ContractDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractDetailSerializer
    
    def get_queryset(self):
        user = self.request.user
        return get_contracts_queryset(user)