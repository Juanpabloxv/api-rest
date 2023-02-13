from rest_framework.test import APITestCase
from .models import Restaurante
from .serializers import RestauranteSerializers
import datetime

class RestauranteTests(APITestCase):
    def setUp(self):
        Restaurante.objects.create(
            nombreRestaurante="Restaurante 1",
            identificacionUsuario=1,
            menu="Comida 1",
            valorMenu=1000,
            fechaPago=datetime.datetime.now(),
            valorPagado=1000
        )
        Restaurante.objects.create(
            nombreRestaurante="Restaurante 2",
            identificacionUsuario=2,
            menu="Comida 2",
            valorMenu=2000,
            fechaPago=datetime.datetime.now(),
            valorPagado=1000
        )
        Restaurante.objects.create(
            nombreRestaurante="Restaurante 3",
            identificacionUsuario=3,
            menu="Comida 3",
            valorMenu=3000,
            fechaPago=datetime.datetime.now(),
            valorPagado=3000
        )

    def test_create_restaurante(self):
        data = {
            "nombreRestaurante": "Restaurante 4",
            "identificacionUsuario": 4,
            "menu": "Comida 4",
            "valorMenu": 4000,
            "fechaPago": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "valorPagado": 4000
        }
        response = self.client.post("/restaurantes/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Restaurante.objects.count(), 4)








