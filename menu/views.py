from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurante
from .serializers import RestauranteSerializers

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.validated_data['valorMenu'] == serializer.validated_data['valorPagado']:
            return Response({"message": "Gracias por pagar todo tu arriendo"}, status=status.HTTP_200_OK)
        elif serializer.validated_data['valorMenu'] > serializer.validated_data['valorPagado']:
            valor_restante = serializer.validated_data['valorMenu'] - serializer.validated_data['valorPagado']
            return Response({"message": f"Gracias por tu abono, sin embargo recuerda que te hace falta pagar ${valor_restante}"}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    

