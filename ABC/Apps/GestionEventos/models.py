from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# Create your models here.


class Usuario(User):
    
    class Meta:
        proxy = True
        ordering = ('first_name', )

def __str__(self):
    return self.name

# class Usuario(models.Model):
#     id = models.AutoField(primary_key=True)
#     Usuario=models.CharField(max_length=50)
#     Contrasena=models.CharField(max_length=50)
#     Correo=models.CharField(max_length=50)

# class Usuario(models.Model):
#     id = models.AutoField(primary_key=True)
#     username=models.CharField(max_length=50)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username=models.CharField(max_length=50)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)

# class Evento(models.Model):
#     Nombre = models.CharField(max_length=50)
#     CATEGORIAS = (('1', 'Conferencia'), ('2', 'Seminario'), ('3', 'Curso'), ('4', 'Congreso'))
#     Categoria = models.CharField(max_length=1, choices=CATEGORIAS, null=False, blank=False)
#     # CATEGORIAS = ('Conferencia', 'Seminario', 'Curso', 'Congreso')
#     # Categoria = models.CharField(max_length=50, choices=CATEGORIAS, null=False, blank=False)
#     Lugar = models.CharField(max_length=50)
#     Direccion = models.CharField(max_length=50)
#     FechaInicio = models.DateTimeField()
#     FechaFin = models.DateTimeField()
#     TIPOS = (('P', 'Presencial'), ('V', 'Virtual'))
#     Tipo = models.CharField(max_length=1, choices=TIPOS, null=False, blank=False)
#     # TIPOS = (('P', 'Presencial'), ('V', 'Virtual'))
#     # Tipo = models.CharField(max_length=1, choices=TIPOS, null=False, blank=False)
#     FechaCreacion = models.DateTimeField(auto_now_add=True)
#     User = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Evento(models.Model):
    event_name = models.CharField(max_length=50)
    CATEGORIAS = (('1', 'Conferencia'), ('2', 'Seminario'), ('3', 'Curso'), ('4', 'Congreso'))
    event_category = models.CharField(max_length=1, choices=CATEGORIAS, null=False, blank=False)
    event_place = models.CharField(max_length=50)
    event_address = models.CharField(max_length=50)
    event_initial_date = models.DateTimeField()
    event_final_date = models.DateTimeField()
    TIPOS = (('P', 'Presencial'), ('V', 'Virtual'))
    event_type = models.CharField(max_length=1, choices=TIPOS, null=False, blank=False)
    # TIPOS = (('P', 'Presencial'), ('V', 'Virtual'))
    # Tipo = models.CharField(max_length=1, choices=TIPOS, null=False, blank=False)
    event_creation_date = models.DateTimeField(auto_now_add=True)
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # event_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=50)
