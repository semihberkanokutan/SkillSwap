from rest_framework.routers import DefaultRouter
from .views import SwapViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'swaps', SwapViewSet)

urlpatterns = [
    path('', include(router.urls))
]