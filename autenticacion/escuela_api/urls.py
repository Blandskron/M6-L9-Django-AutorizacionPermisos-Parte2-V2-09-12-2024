from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EscuelaViewSet

router = DefaultRouter()
router.register(r'escuelas', EscuelaViewSet, basename='escuela')

urlpatterns = [
    path('', include(router.urls)),
]
