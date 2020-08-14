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
    return self.first_name

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
    event_creation_date = models.DateTimeField(auto_now_add=True)
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail = models.ImageField("Imagen", upload_to="event_thumbnails", default="event_thumbnails/default.png")

def __str__(self):
    return self.event_name
