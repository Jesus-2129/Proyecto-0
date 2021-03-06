"""ABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ABC.Apps.GestionEventos.api import UserAPI
from rest_framework.authtoken import views
from ABC.Apps.GestionEventos.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', Login.as_view(), name='Login'),
    path('admin/', admin.site.urls),
    path('api/create-user/', UserAPI.as_view() , name = 'api_create_user'),
    path('api/events/', EventoList2.as_view(), name = 'evento_list'), #esto es back

    path('api/api-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/events/<int:evento_id>/', EventoDetalle.as_view(), name = 'detalle_evento_list'),


    # path('evento/',Lista_Eventos.as_view(), name = 'Lista_eventos'),
    path('api/eventos/',Listado_Eventos, name = 'Listado_Eventos'),
    path('api/events/delete/<int:evento_id>',Eliminar_Evento, name = 'Eliminar_Eventos'),
    path('api/events/update/<int:evento_id>',Modificar_Evento2, name = 'Modificar_Eventos'),
    path('api/events/create/', Crear_Evento, name = 'crear_evento'),
    # path('api/create-user-2/', Crear_Usuario, name = 'Nuevo_Usuario'),
    path('api/create-user-2/', Usuario_Nuevo.as_view(), name = 'Nuevo_Usuario'),

]
