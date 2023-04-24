from django.urls import path
from .views import UserList, UserDetail, SignupView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('list/', UserList.as_view(), name="accounts_list"),
    path('list/<int:pk>', UserDetail.as_view(), name="accounts_details"),
    path('signup/', SignupView.as_view(), name='accounts_signup'),
    path("login/", TokenObtainPairView.as_view(), name="login_obtain_tokens"),
]