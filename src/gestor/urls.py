from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropiedadViewSet, PropietarioViewSet

router = DefaultRouter()

router.register(r'propietarios', PropietarioViewSet)
router.register(r'propiedades', PropiedadViewSet)

urlpatterns = [
    path('', include(router.urls))
]
