from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Propiedad(models.Model):
    TIPOS_PROPIEDAD = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamentp'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno'),
    ]
    
    direccion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPOS_PROPIEDAD)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='propiedades')
    
    def __str__(self):
        return f'{self.tipo} en {self.direccion}'