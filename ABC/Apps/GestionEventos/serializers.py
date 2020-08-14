from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Evento, Usuario


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.email = validate_data.get('email')
        # instance.set_password = validate_data.get('password')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError(
                "Este nombre de usuario ya existe")
        else:
            return data

    def validate_email(self, data):
        emails = User.objects.filter(email=data)
        if len(emails) != 0:
            raise serializers.ValidationError("Este correo ya fue usado")
        else:
            return data

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

    def create(self, validate_data):
        instance = Evento()
        instance.event_name = validate_data.get('event_name')
        instance.event_category = validate_data.get('event_category')
        instance.event_place = validate_data.get('event_place')
        instance.event_address = validate_data.get('event_address')
        instance.event_initial_date = validate_data.get('event_initial_date')
        instance.event_final_date = validate_data.get('event_final_date')
        instance.event_type = validate_data.get('event_type')
        instance.thumbnail = validate_data.get('thumbnail')
        instance.event_user = validate_data.get('event_user')
        instance.save()
        return instance

    def update(self, instance, validate_data):
        instance.event_name = validate_data.get('event_name',instance.event_name)
        instance.event_category = validate_data.get('event_category', instance.event_category)
        instance.event_place = validate_data.get('event_place', instance.event_place)
        instance.event_address = validate_data.get('event_address', instance.event_address)
        instance.event_initial_date = validate_data.get('event_initial_date', instance.event_initial_date)
        instance.event_final_date = validate_data.get('event_final_date', instance.event_final_date)
        instance.event_type = validate_data.get('event_type',instance.event_type)
        instance.thumbnail = validate_data.get('thumbnail' , instance.thumbnail)
        instance.event_user = validate_data.get('event_user', instance.event_user)

        instance.save()
        return instance