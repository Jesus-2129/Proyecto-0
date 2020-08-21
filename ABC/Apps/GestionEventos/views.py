from django.shortcuts import render, redirect
from django.template import RequestContext
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
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
from rest_framework.renderers import TemplateHTMLRenderer #para templates
from django.views.generic import TemplateView #para templates
from django.views import View
from .forms import EventoForm, UsuarioForm

# Create your views here.

class Usuario_Nuevo(APIView, TemplateView):
    template_name = "registro.html"

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://127.0.0.1:8000')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def Crear_Usuario(request):
    formularioUsr = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        print(form)
        if form.is_valid():
            print("Entro")
            form.set_password(form.password)
            form.save()
            return redirect("http://127.0.0.1:8000")
        else:
            return render(request,'registro.html', {'formulario': formularioUsr})
    else:
        formularioUsr = UsuarioForm()
    return render(request,'registro.html', {'formulario': formularioUsr})    

@csrf_exempt
def Crear_Evento(request):
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    usere = request.user
    formularioIns = EventoForm()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        evento = Evento(event_name=form['event_name'].value(), event_category=form['event_category'].value(), event_place=form['event_place'].value(), event_address=form['event_address'].value(), event_initial_date=form['event_initial_date'].value(), event_final_date=form['event_final_date'].value(), event_type=form['event_type'].value(), thumbnail=form['thumbnail'].value(),event_user=usere)
        evento.save()
            
        return render(request, 'registro3.html', {'formulario':formularioIns})

    else:
        formularioIns = EventoForm()

    return render(request, 'InsEvento.html', {'formulario':formularioIns})

@csrf_exempt
def Listado_Eventos(request):
    user = request.user.id
    queryset = Evento.objects.filter(event_user=user)
    serializer_class = EventoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    return render(request, 'P4.html',{'queryset':queryset})

@csrf_exempt
def Eliminar_Evento(request, evento_id):
    user = request.user.id
    queryset = Evento.objects.filter(event_user=user)
    try:
        eventos = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        raise Http404
    eventos.delete()
    return redirect("http://127.0.0.1:8000/api/eventos/")  

@csrf_exempt
def Modificar_Evento2(request, evento_id):  
    user = request.user.id
    usere = request.user
    eventos = Evento.objects.get(event_user=user, id=evento_id) 
    form = EventoForm(request.POST, instance = eventos)
    print(form)
    print(eventos)
    print('Voy a entrar al formulario')  
    if form.is_valid():
        print('Entre al formulario')  
        form.save()  
        return redirect("http://127.0.0.1:8000/api/eventos/")  
    return render(request, 'actualiza_evento.html', {'eventos': eventos, 'formulario':form}) 

class Lista_Eventos(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class EventoList2(APIView, TemplateView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'InsEvento.html'
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get(self, request):
        user = request.user.id
        eventos = Evento.objects.filter(event_user=user)
        serializer = serializers.EventoSerializer(eventos, many=True)
        return Response(serializer.data,  template_name='registro2.html')

    def post(self, request):
        serializer = serializers.EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, template_name = 'registro2.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name = 'InsEvento.html')


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
        serializer = serializers.EventoSerializer(
            eventos, data=request.data, partial=True)
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

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("Listado_Eventos")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)