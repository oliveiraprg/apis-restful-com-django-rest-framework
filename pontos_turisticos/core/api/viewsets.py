from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    
    serializer_class = PontoTuristicoSerializer
    queryset = PontoTuristico.objects.all()