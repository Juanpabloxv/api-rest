from menu.models import Restaurante
from rest_framework import viewsets, permissions
from menu.serializers import RestauranteSerializers

class RestauranteVisewsets(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class = RestauranteSerializers