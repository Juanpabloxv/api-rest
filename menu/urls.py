from rest_framework import routers
from .api import RestauranteVisewsets

router = routers.DefaultRouter()
router.register('api/pagos', RestauranteVisewsets, 'Menu')
router.register('api/pagos', RestauranteVisewsets, 'Menu')
urlpatterns = router.urls