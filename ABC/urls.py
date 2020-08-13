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
from ABC.Apps.GestionEventos.views import EventoList, Login, EventoViewSet, UsuarioList
from rest_framework.authtoken import views

# evento_list = EventoViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-user/', UserAPI.as_view() , name = 'api_create_user'),
    path('api/events/', EventoList.as_view(), name = 'evento_list'),
    path('api/api-auth/', views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'Login'),
    path('Lista_usuarios/', UsuarioList.as_view(), name = 'lista_usuarios_faq'),
]
