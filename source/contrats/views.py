from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer, ContractDetailSerializer
from .models import Contract
from events.models import Event
from rest_framework.permissions import IsAuthenticated


class ContractList(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ContractListSerializer
    def get_queryset(self):
        user = self.request.user
        if user.role =="SALE":
            return Contract.objects.filter(sales_contract_id=user.id)
        elif user.role == "SUPPORT":
            list_contracts = []
            list_events = Event.objects.filter(support_events=user.id)
            for i in list_events:
                list_contracts.append(i.contract_events_id)
            return Contract.objects.filter(id__in=list_contracts)       
        else:
            return Contract.objects.all()



class ContractDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer