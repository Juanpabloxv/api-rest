from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nombreRestaurante = models.CharField(max_length=200)
    identificacionUsuario = models.CharField(max_length=200)
    menu = models.CharField(max_length=200)
    valorMenu = models.IntegerField()
    fechaPago = models.DateTimeField(auto_now_add=True)
    valorPagado = models.IntegerField()
