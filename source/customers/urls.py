from django.urls import path
from .views import CustomersList, CustomersDetail

urlpatterns = [
    path('list/', CustomersList.as_view(), name="customer_list"),
    path('list/<int:pk>/', CustomersDetail.as_view(), name="customer_details"),
]