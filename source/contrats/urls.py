from django.urls import path
from .views import ContractList

urlpatterns = [
    path('list/', ContractList.as_view()),
]