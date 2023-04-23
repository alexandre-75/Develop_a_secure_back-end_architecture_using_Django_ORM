from django.urls import path
from .views import UserList

urlpatterns = [
    path('list/', UserList.as_view()),
]