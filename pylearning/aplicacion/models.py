from django.db import models

class Usuario(models.Model):

    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
