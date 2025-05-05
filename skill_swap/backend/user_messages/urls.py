from rest_framework.routers import DefaultRouter
from .views import UserMessageViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'user_messages', UserMessageViewSet)

urlpatterns = [
    path('', include(router.urls))
]