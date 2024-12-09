from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgenteViewSet, InmuebleViewSet, ProspectoViewSet, transacciones_recientes

router = DefaultRouter()
router.register('agentes', AgenteViewSet)
router.register('inmuebles', InmuebleViewSet)
router.register('prospectos', ProspectoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/transacciones-recientes/', transacciones_recientes, name='transacciones-recientes'),
]