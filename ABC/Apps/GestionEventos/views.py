from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Evento, Usuario
from .serializers import EventoSerializer, UserSerializer
from . import serializers
from django.http import Http404

# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class Eventos(APIView):

    def get(self, request, usuario_id):
        eventos = Evento.objects.filter(usuario__id=usuario_id)
        serializer = serializers.EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request, usuario_id):
        try:
            Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            raise Http404

        serializer = serializers.EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario_id=usuario_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventosDetalle(APIView):

    def get(self, request, usuario_id, evento_id):
        try:
            evento = Evento.objects.get(usuario__id=usuario_id, pk=evento_id)
        except Evento.DoesNotExist:
            raise Http404
        serializer = serializers.EventoSerializer(evento)
        return Response(serializer.data)

    def delete(self, request, usuario_id, evento_id):
        try:
             evento = Evento.objects.get(usuario__id=usuario_id, pk=evento_id)
        except Evento.DoesNotExist:
            raise Http404
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class UsuarioList(generics.ListCreateAPIView):
    # template_name = "eventos.html"
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class EventoList(generics.ListCreateAPIView):
    # template_name = "eventos.html"
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

#Este si sirve

class EventoList2(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        eventos = Evento.objects.filter(event_user=user)
        serializer = serializers.EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # user = request.user.id
        # try:
        #     Usuario.objects.get(pk=Usuario.id)
        # except Usuario.DoesNotExist:
        #     raise Http404

        serializer = serializers.EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoDetalle(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, evento_id):
        user = request.user.id
        eventos = Evento.objects.filter(event_user=user, id=evento_id)
        serializer = serializers.EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def put(self, request, evento_id):
        user = request.user.id 
        eventos = Evento.objects.get(event_user=user, id=evento_id)
        serializer = serializers.EventoSerializer(eventos, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            eventos_guardado = serializer.save()
        # eventos.update()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, evento_id):
        try:
            eventos = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            raise Http404
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
        # user = request.user.id
        # eventos = Evento.objects.filter(event_user=user, id=evento_id)
        # eventos.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)  

# class Login(FormView):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('admin/')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(Login, self).dispatch(request, *args, *kwargs)

#     def form_valid(self, form):
#         user = authenticate(
#             username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#         token, _ = Token.objects.get_or_create(user=user)
#         if token:
#             login(self.request, form.get_user())
#             return super(Login, self).form_valid(form)


# class Logout(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         logout(request)
#         return Response(status=status.HTTP_200_OK)


class EventoViewSet(generics.ListCreateAPIView):
    querysey = Evento.objects.all()
    serializer_class = EventoSerializer
