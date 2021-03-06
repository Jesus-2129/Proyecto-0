# Generated by Django 3.1 on 2020-08-12 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestionEventos', '0004_auto_20200811_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='Direccion',
            new_name='event_address',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='Categoria',
            new_name='event_category',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='Lugar',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='Nombre',
            new_name='event_place',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='Tipo',
            new_name='event_type',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='FechaCreacion',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='FechaFin',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='FechaInicio',
        ),
        migrations.AddField(
            model_name='evento',
            name='event_creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='event_final_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='event_initial_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='thumbnail',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
