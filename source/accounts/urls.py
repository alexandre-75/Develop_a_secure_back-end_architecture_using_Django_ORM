from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('list/', UserList.as_view(), name="accounts_list"),
    path('list/<int:pk>', UserDetail.as_view(), name="accounts_details"),
]