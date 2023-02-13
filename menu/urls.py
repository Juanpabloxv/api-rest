from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet

router = DefaultRouter()
router.register('api/pagos', RestauranteViewSet, basename='pagos')

urlpatterns = [
    path('', include(router.urls)),
]
