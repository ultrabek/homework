from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CarViewSet

router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register('cars', CarViewSet)

urlpatterns = router.urls