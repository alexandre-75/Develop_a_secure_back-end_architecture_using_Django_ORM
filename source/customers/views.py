from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomersListSerializer, CustomersDetailSerializer
from .models import Client
from events.models import Event


class CustomersList(ListAPIView, CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = CustomersListSerializer
    
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


class CustomersDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = CustomersDetailSerializer
    
