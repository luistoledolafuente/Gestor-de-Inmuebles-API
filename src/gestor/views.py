from rest_framework import viewsets, filters
from .models import Propiedad, Propietario
from .serializers import PropiedadSerializers, PropietarioSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializers
    
    #Aqui implementamos los filtros
    filter_backends = [filters.SearchFilter]
    search_fields = ['direccion', 'tipo']