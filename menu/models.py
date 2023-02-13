from django.db import models
from django.core.exceptions import ValidationError

    
class Restaurante(models.Model):
    nombreRestaurante = models.CharField(max_length=200)
    identificacionUsuario = models.IntegerField()
    menu = models.CharField(max_length=200)
    valorMenu = models.IntegerField()
    fechaPago = models.DateTimeField()
    valorPagado = models.IntegerField()
