from rest_framework import viewsets
from .models import Services
from .serializers import ServicesSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer