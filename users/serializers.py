from rest_framework import serializers
from .models import Tenant

class TenantSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'email', 'phone', 'created_at']