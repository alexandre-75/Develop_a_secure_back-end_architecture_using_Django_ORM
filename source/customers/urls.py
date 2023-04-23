from django.urls import path
from .views import CustomersList

urlpatterns = [
    path('list/', CustomersList.as_view()),
]