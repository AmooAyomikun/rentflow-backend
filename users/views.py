from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tenant
from .serializers import TenantSerialzer

class TenantListView(APIView):
    def get(self, request):
        tenants = Tenant.objects.all()
        serializer = TenantSerialzer(tenants, many=True)
        return Response({
            'success': True,
            'message': 'Tenants retrieved',
            'data': serializer.data
        })

    def post(self, request):
        serializer = TenantSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Tenant created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'success': True,
            'message': 'Tenant created successfully',
            'data': {'id': tenant.id, 'name': tenant.name}
        }, status=status.HTTP_201_CREATED)

