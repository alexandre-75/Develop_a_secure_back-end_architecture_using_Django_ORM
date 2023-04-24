from rest_framework.serializers import ModelSerializer
from .models import Contract


class ContractListSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = ["id"]