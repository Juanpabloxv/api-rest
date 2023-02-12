from rest_framework import serializers
from .models import Restaurante

class RestauranteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'nombreRestaurante','identificacionUsuario','menu','valorMenu','fechaPago','valorPagado')




       