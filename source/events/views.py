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
        if user.role == "SALE":
            return Event.objects.filter(sales_events=user.id)
        elif user.role == "SUPPORT":
            return Event.objects.filter(support_events=user.id)
        else:
            return Event.objects.all()
   

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