from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'compact', CompactcarViewSet)
router.register(r'sedan', SedansViewSet)
router.register(r'suv', SuvViewSet)
router.register(r'van', VansViewSet)
router.register(r'truck', TrucksViewSet)
router.register(r'luxury', LuxurycarsViewSet)
router.register(r'convertible', ConvertiblesViewSet)
router.register(r'ev-hybrid', Electriccars_HybridsViewSet)
router.register(r'sports', SportscarsViewSet)
router.register(r'motorcycle', MotorcyclesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]