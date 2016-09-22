from django.contrib import admin

from ..models import (
    CategoriaEvento,
    CodigoVerificacion,
    CentroDonacion,
    Direccion,
    Donacion,
    Donante,
    EstadoDonacion,
    Evento,
    GrupoSanguineo,
    GrupoSanguineoSolicitud,
    HistoricoEstadoDonacion,
    ImagenEvento,
    Localidad,
    LugarDonacion,
    LugarEvento,
    Nacionalidad,
    Provincia,
    RegistroDonacion,
    SolicitudDonacion,
    TipoCentroDonacion,
    TipoDocumento,
    TipoSolicitudDonacion,
    VerificacionDonacion,
    Paciente,
    ImagenSolicitudDonacion
    )

from .codigoverificacion import CodigoVerificacionAdmin

admin.site.register(CodigoVerificacion, CodigoVerificacionAdmin)
admin.site.register(CategoriaEvento)
admin.site.register(CentroDonacion)
admin.site.register(TipoCentroDonacion)
admin.site.register(Donante)
admin.site.register(GrupoSanguineo)
admin.site.register(SolicitudDonacion)
admin.site.register(TipoSolicitudDonacion)
admin.site.register(RegistroDonacion)
admin.site.register(Donacion)
admin.site.register(HistoricoEstadoDonacion)
admin.site.register(EstadoDonacion)
admin.site.register(GrupoSanguineoSolicitud)
admin.site.register(Evento)
admin.site.register(ImagenEvento)
admin.site.register(Direccion)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(Nacionalidad)
admin.site.register(TipoDocumento)
admin.site.register(LugarDonacion)
admin.site.register(LugarEvento)
admin.site.register(VerificacionDonacion)
admin.site.register(Paciente)
admin.site.register(ImagenSolicitudDonacion)
