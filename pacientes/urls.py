from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, ConsultaViewSet, ExameViewSet, ProntuarioViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'prontuarios', ProntuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
