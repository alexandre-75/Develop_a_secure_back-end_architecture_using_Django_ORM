from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import EventListSerializer, EventDetailSerializer
from .models import Event


class EventList(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer