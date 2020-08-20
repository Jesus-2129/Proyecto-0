from django.forms import ModelForm
from .models import Usuario, Evento

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ('event_name', 'event_category', 'event_place', 'event_address', 'event_initial_date', 'event_final_date', 'event_type', 'thumbnail')

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
