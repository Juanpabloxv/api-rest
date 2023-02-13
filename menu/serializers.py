from rest_framework import serializers
from .models import Restaurante
from datetime import datetime

def validate_fecha_pago(value):
    fecha = datetime.strptime(value.strftime("%d/%m/%Y"), "%d/%m/%Y")
    if fecha.day % 2 == 0:
        raise serializers.ValidationError("Lo siento pero no se puede recibir el pago por decreto de administración")
    return value

def validate_nombre_restaurante(value):
    if not isinstance(value, str):
        raise serializers.ValidationError("Formato de nombre incorrecto")
    return value

def validate_identificacion_usuario(value):
    try:
        int(value)
    except ValueError:
        raise serializers.ValidationError("La identificación de usuario debe ser un número.")
    return value

def validate_valor_pagado(value):
    if value < 1 or value > 1000000:
        raise serializers.ValidationError("El valor pagado debe estar entre 1 y 1000000")
    return value

def validate_valor_menu(value):
    if value < 0 or value > 1000000:
        raise serializers.ValidationError("No se reciben valores negativos")
    return value

class RestauranteSerializers(serializers.ModelSerializer):
    nombreRestaurante = serializers.CharField(validators=[validate_nombre_restaurante])
    identificacionUsuario = serializers.CharField(validators=[validate_identificacion_usuario])
    fechaPago = serializers.DateTimeField(validators=[validate_fecha_pago])
    valorPagado = serializers.IntegerField(validators=[validate_valor_pagado])
    valorMenu = serializers.IntegerField(validators=[validate_valor_menu])
    class Meta:
        model = Restaurante
        fields = ('id', 'nombreRestaurante','identificacionUsuario','menu','valorMenu','fechaPago','valorPagado')




       