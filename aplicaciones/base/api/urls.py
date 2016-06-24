"""manosxgotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from .views import (
    DonanteListAPI,
    GrupoSanguineoListAPI,
    NacionalidadListAPI,
    TipoDocumentoListAPI
    )

urlpatterns = [
    # Listados atributos del donante
    url(r'^listado-donantes/$', DonanteListAPI.as_view() , name='listado-donantes'),
    url(r'^listado-grupos-sanguineos/$', GrupoSanguineoListAPI.as_view() , name='listado-grupos-sanguineos'),
    url(r'^listado-nacionalidades/$', NacionalidadListAPI.as_view() , name='listado-nacionalidades'),
    url(r'^listado-tipos-documentos/$', TipoDocumentoListAPI.as_view() , name='listado-tipos-documentos'),

    # Urls de aplicaciones
    url(r'^cuentas/', include('aplicaciones.cuentas.api.urls', namespace='cuentas')),
    url(r'^donantes/', include('aplicaciones.donantes.api.urls', namespace='donantes')),
    url(r'^direcciones/', include('aplicaciones.direcciones.api.urls', namespace='direcciones')),

]