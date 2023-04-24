from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import EventListSerializer, EventDetailSerializer
from .models import Event


class EventList(ListAPIView):
    
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer