from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agente, Inmueble, Prospecto, Transaccion
from .serializers import AgenteSerializer, InmuebleSerializer, ProspectoSerializer, TransaccionSerializer

class AgenteViewSet(ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class InmuebleViewSet(ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class ProspectoViewSet(ModelViewSet):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer

@api_view(['GET'])
def transacciones_recientes(request):
    transacciones = Transaccion.objects.order_by('-fecha')[:5]
    serializer = TransaccionSerializer(transacciones, many=True)
    return Response(serializer.data)
