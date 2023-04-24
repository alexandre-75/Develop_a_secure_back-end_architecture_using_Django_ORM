from django.urls import path
from .views import ContractList, ContractDetail

urlpatterns = [
    path('list/', ContractList.as_view(), name="contract_list"),
    path('list/<int:pk>/', ContractDetail.as_view(), name="contract_details"),
]