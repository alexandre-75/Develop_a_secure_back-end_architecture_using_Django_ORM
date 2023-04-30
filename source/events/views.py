from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import EventListSerializer, EventDetailSerializer
from .models import Event
from .permissions import EventPermissions


class EventList(ListAPIView):
    
    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventListSerializer
    
    def get_queryset(self):
        user = self.request.user
        print(user)
        
        client_name = self.request.query_params.get('first_name')
        client_email = self.request.query_params.get('email')
        date_created_event = self.request.query_params.get('event_date')
        
        queryset = Event.objects.all()
        
        if user.role == "SALE":
            queryset = Event.objects.filter(sales_events=user.id)
            if date_created_event:
                queryset = queryset.filter(event_date__icontains=date_created_event)
            elif client_name:
                queryset = queryset.filter(client_event_id__first_name__icontains=client_email)
            elif client_email:
                queryset = queryset.filter(client_event_id__email__icontains=client_email)
            else:
                pass
        elif user.role == "SUPPORT":
            queryset = Event.objects.filter(support_events=user.id)
            if date_created_event:
                queryset = queryset.filter(event_date__icontains=date_created_event)
            elif client_name:
                queryset = queryset.filter(client_event_id__first_name__icontains=client_email)
            elif client_email:
                queryset = queryset.filter(client_event_id__email__icontains=client_email)
            else:
                pass
        return queryset
   

class EventDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated, EventPermissions]
    serializer_class = EventDetailSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.role == "SALE":
            return Event.objects.filter(sales_events=user.id)
        elif user.role == "SUPPORT":
            return Event.objects.filter(support_events=user.id)
        else:
            return Event.objects.all()