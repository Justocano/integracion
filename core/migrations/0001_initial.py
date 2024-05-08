# Generated by Django 5.0.4 on 2024-05-04 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre categoría')),
            ],
            options={
                'verbose_name': 'Categoría de producto',
                'verbose_name_plural': 'Categorías de productos',
                'db_table': 'Categoria',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Comuna')),
                ('descripcion', models.CharField(max_length=400, verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to='productos/', verbose_name='Imagen')),
                ('Clase', models.CharField(max_length=100, verbose_name='Clase')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'Comuna',
                'ordering': ['id', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del servicio')),
                ('descripcion', models.CharField(max_length=400, verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.ImageField(upload_to='productos/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'Servicio',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(choices=[('Cliente', 'Cliente'), ('Administrador', 'Administrador'), ('Superusuario', 'Superusuario')], max_length=50, verbose_name='Tipo de usuario')),
                ('rut', models.CharField(max_length=15, verbose_name='RUT')),
                ('direccion', models.CharField(max_length=400, verbose_name='Dirección')),
                ('subscrito', models.BooleanField(verbose_name='Subscrito')),
                ('imagen', models.ImageField(upload_to='perfiles/', verbose_name='Imagen')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de usuarios',
                'db_table': 'Perfil',
                'ordering': ['tipo_usuario'],
            },
        ),
    ]