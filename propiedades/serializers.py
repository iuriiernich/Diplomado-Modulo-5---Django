from rest_framework import serializers
from .models import Agente, Inmueble, Prospecto, Transaccion

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = '__all__'

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'

class ProspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospecto
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'
