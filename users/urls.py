from django.urls import path
from .views import TenantListView

urlPatterns = [
    path('tenants/', TenantListView.as_view(), name='tenant-list'),
]

