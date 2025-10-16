from rest_framework import serializers
from .models import Propiedad, Propietario

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'
        
class PropiedadSerializers(serializers.ModelSerializer):
    propiedad_nombre = serializers.CharField(source='propietario', read_only=True)
    class Meta:
        model = Propiedad
        fields = ['id', 'direccion', 'precio', 'tipo', 'propietario', 'propiedad_nombre']
        extra_kwargs = {
            'propietario': {'write_only': True}
        }