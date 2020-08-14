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
# Este si sirve

class EventoList2(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        eventos = Evento.objects.filter(event_user=user)
        serializer = serializers.EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, evento_id):
        try:
            eventos = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            raise Http404
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)