from django.contrib import admin
from .models import Agente, Inmueble

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('direccion','precio','descripcion','status','agente')
