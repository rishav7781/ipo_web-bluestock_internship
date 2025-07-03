from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import IPO
from .serializers import IPOSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'company_name']
