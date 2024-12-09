from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
import re

def validate_price(value):
    if value <= 0:
        raise ValidationError("El precio debe ser mayor que cero.")

def validate_phone(value):
    if len(value) != 8 or not value.isdigit():
        raise ValidationError("El número de teléfono debe tener 8 dígitos.")

class Agente(models.Model):
    TIPOS_DOCUMENTOS = [
        ('CI', 'Carnet de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PP', 'Pasaporte')
    ]
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTOS)
    numero_documento = models.CharField(
        max_length=20, 
        unique=True,
        validators=[
            MinLengthValidator(6, "Número de documento debe tener al menos 6 caracteres"),
        ]
    )
    telefono = models.CharField(max_length=8, validators=[validate_phone])
    email = models.EmailField(unique=True)

    def clean(self):
        # Validación de número de documento
        if not re.match(r'^\d+$', self.document_number):
            raise ValidationError("Número de documento solo debe contener números")

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    TIPOS_INMUEBLES = [
        ('CASA', 'Casa'),
        ('APARTAMENTO', 'Apartamento'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno')
    ]

    ESTADOS_INMUEBLES = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('VENDIDO', 'Vendido')
    ]
    tipo_inmueble = models.CharField(max_length=15, choices=TIPOS_INMUEBLES)

    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    descripcion = models.TextField(blank=True)
    status = models.CharField(
        max_length=15, 
        choices=ESTADOS_INMUEBLES,  
        default='DISPONIBLE'
    )
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion

class Prospecto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[validate_phone])
    email = models.EmailField(unique=True)
    interested_properties = models.ManyToManyField(Inmueble, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    prospecto = models.ForeignKey(Prospecto, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transacción {self.inmueble} - {self.prospecto}"
