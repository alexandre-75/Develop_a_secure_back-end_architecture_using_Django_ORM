from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ContractListSerializer, ContractDetailSerializer
from .models import Contract
from customers.models import Client
from events.models import Event
from rest_framework.permissions import IsAuthenticated
from .permissions import ContractPermissions
from django.db.models import Q





class ContractList(ListAPIView):
    
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractListSerializer
    
    def get_queryset(self):
        
        user = self.request.user
        
        client_name = self.request.query_params.get('first_name')
        client_email = self.request.query_params.get('email')
        amount_contract = self.request.query_params.get('amount')
        date_created_contract = self.request.query_params.get('date_created')

        
        if user.role == "SALE":
            queryset = Contract.objects.filter(sales_contract_id=user.id)
            if amount_contract:
                queryset = queryset.filter(amount__icontains=amount_contract) 
            elif date_created_contract:
                queryset = queryset.filter(date_created__icontains=date_created_contract) 
            elif client_email:
                queryset = queryset.filter(client_contract_id__email__icontains=client_email)
            elif client_name:
                queryset = queryset.filter(client_contract_id__first_name__icontains=client_name)
            else:
                pass      
        elif user.role == "SUPPORT":
            list_events = Event.objects.filter(support_events=user.id)
            list_contracts = [event.contract_events_id for event in list_events]
            queryset = Contract.objects.filter(id__in=list_contracts)
            if amount_contract:
                queryset = queryset.filter(amount__icontains=amount_contract) 
            elif date_created_contract:
                queryset = queryset.filter(date_created__icontains=date_created_contract) 
            elif client_email:
                queryset = queryset.filter(client_contract_id__email__icontains=client_email)
            elif client_name:
                queryset = queryset.filter(client_contract_id__first_name__icontains=client_name)
            else:
                pass 
        elif user.role == "MANAGEMENT":
            queryset = Contract.objects.all()
            if amount_contract:
                queryset = queryset.filter(amount__icontains=amount_contract) 
            elif date_created_contract:
                queryset = queryset.filter(date_created__icontains=date_created_contract) 
            elif client_email:
                queryset = queryset.filter(client_contract_id__email__icontains=client_email)
            elif client_name:
                queryset = queryset.filter(client_contract_id__first_name__icontains=client_name)
            else:
                pass 
            
        return queryset

class ContractDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView):
    
    permission_classes = [IsAuthenticated, ContractPermissions]
    serializer_class = ContractDetailSerializer
    
    def get_queryset(self):

        user = self.request.user
        queryset = Contract.objects.all()

        if user.role == "SALE":
            queryset = Contract.objects.filter(sales_contract_id=user.id)
        elif user.role == "SUPPORT":
            list_events = Event.objects.filter(support_events=user.id)
            list_contracts = [event.contract_events_id for event in list_events]
            return Contract.objects.filter(id__in=list_contracts)
        return queryset