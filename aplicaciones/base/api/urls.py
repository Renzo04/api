from django.conf.urls import include, url

from .views import (
    CentroDonacionListAPI,
    CentroDonacionInfoAPI,
    DonanteListAPI,
    EventoListAPI,
    EventoInfoAPI,
    GrupoSanguineoListAPI,
    NacionalidadListAPI,
    TipoDocumentoListAPI
    )

urlpatterns = [
    # Listados atributos del donante
    url(r'^listado-donantes/$', DonanteListAPI.as_view(), name='listado-donantes'),
    url(r'^listado-grupos-sanguineos/$', GrupoSanguineoListAPI.as_view(), name='listado-grupos-sanguineos'),
    url(r'^listado-nacionalidades/$', NacionalidadListAPI.as_view(), name='listado-nacionalidades'),
    url(r'^listado-tipos-documentos/$', TipoDocumentoListAPI.as_view(), name='listado-tipos-documentos'),
    url(r'^listado-centros-donacion/$', CentroDonacionListAPI.as_view(), name='listado-centros-donacion'),
    url(r'^centro/(?P<id>\w+)$', CentroDonacionInfoAPI.as_view(), name='detalle-centro'),
    url(r'^evento/(?P<id>\w+)$', EventoInfoAPI.as_view(), name='detalle-evento'),
    url(r'^listado-eventos/$', EventoListAPI.as_view(), name='listado-eventos'),

    # Urls de aplicaciones
    url(r'^cuentas/', include('aplicaciones.cuentas.api.urls', namespace='cuentas')),
    url(r'^donantes/', include('aplicaciones.donantes.api.urls', namespace='donantes')),
    url(r'^direcciones/', include('aplicaciones.direcciones.api.urls', namespace='direcciones')),
    url(r'^donaciones/', include('aplicaciones.donaciones.api.urls', namespace='donaciones')),
]
