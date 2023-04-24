from django.urls import path
from .views import EventList, EventDetail

urlpatterns = [
    path('list/', EventList.as_view(), name="event_list"),
    path('list/<int:pk>/', EventDetail.as_view(), name="event_details"),
]