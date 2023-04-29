from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomersListSerializer, CustomersDetailSerializer
from .models import Client
from events.models import Event
from .permissions import ClientPermissions
from django.contrib.auth.models import Group, Permission
from django.db.models import Q


class CustomersList(ListAPIView, CreateAPIView):
    
    permission_classes = [IsAuthenticated, ClientPermissions]
    serializer_class = CustomersListSerializer
    
    def get_queryset(self):
        user = self.request.user
        client_name = self.request.query_params.get('first_name')
        client_email = self.request.query_params.get('email')

        queryset = Client.objects.all()

        if user.role == "SALE":
            queryset = queryset.filter(sales_client=user)
            if client_name:
                queryset = queryset.filter(first_name__icontains=client_name)      
            elif client_email:
                queryset = queryset.filter(email__icontains=client_email)
            else:
                pass
        elif user.role == "SUPPORT":
            if client_name:
                queryset = queryset.filter(first_name__icontains=client_name)
            elif client_email:
                queryset = queryset.filter(email__icontains=client_email)
            else: 
                list_clients = Event.objects.filter(support_events=user.id).values_list('client_events_id', flat=True)
                queryset = queryset.filter(id__in=list_clients)     
        return queryset


class CustomersDetail(RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated, ClientPermissions]
    serializer_class = CustomersDetailSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.role == "SALE":
            return Client.objects.filter(sales_client=user)     
        elif user.role == "SUPPORT":
            list_clients = []
            list_events = Event.objects.filter(support_events=user.id)
            for i in list_events:
                list_clients.append(i.client_events_id)
            return Client.objects.filter(id__in=list_clients)
        else: 
            return Client.objects.all()