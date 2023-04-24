from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('accounts/', include('accounts.urls')),
    path('contracts/', include('contrats.urls')),
    path('events/', include('events.urls')),
]
