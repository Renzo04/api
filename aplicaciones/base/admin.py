from django.contrib import admin

from .models import *

admin.site.register(CentroDonacion)
admin.site.register(TipoCentroDonacion)
admin.site.register(Donante)
admin.site.register(GrupoSanguineo)
admin.site.register(SolicitudDonacion)
admin.site.register(TipoSolicitudDonacion)
admin.site.register(EstadoSolicitudDonacion)
admin.site.register(RegistroDonacion)
admin.site.register(Donacion)
admin.site.register(HistoricoEstadoDonacion)
admin.site.register(EstadoDonacion)
admin.site.register(GrupoSanguineoSolicitud)
admin.site.register(Evento)
admin.site.register(Direccion)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(Nacionalidad)
admin.site.register(TipoDocumento)