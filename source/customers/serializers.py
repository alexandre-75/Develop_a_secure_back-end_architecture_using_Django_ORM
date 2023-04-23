from rest_framework.serializers import ModelSerializer
from .models import Client

"""
    serializers are a key component of Django REST Framework,
    that manage the conversion of data between Python and JSON formats for REST APIs.
"""


class CustomersSerializer(ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"