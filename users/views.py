from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tenant

class TenantListView(APIView):
    def get(self, request):
        tenants = Tenant.objects.all()
        tenant_list = []
        for tenant in tenants:
            tenant_list.append({
                'id': tenant.id,
                'name': tenant.name,
                'email': tenant.email,
                'phone': tenant.phone
            })
        return Response({
            'success': True,
            'message': 'Tenants retrieved',
            'data': tenant_list
        })

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')

        tenant = Tenant.objects.create(
            name=name,
            email=email,
            phone=phone
        )

        return Response({
            'success': True,
            'message': 'Tenant created successfully',
            'data': {'id': tenant.id, 'name': tenant.name}
        }, status=status.HTTP_201_CREATED)

