from rest_framework.routers import DefaultRouter
from .views import MtmFirstViewSet, MtmSecondViewSet, MtoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('MtmFirst', MtmFirstViewSet, basename='first')
router.register('MtmSecond', MtmSecondViewSet, basename='second')
router.register('Mto', MtoViewSet, basename='mto')

urlpatterns = [
    path('', include(router.urls)),
]
