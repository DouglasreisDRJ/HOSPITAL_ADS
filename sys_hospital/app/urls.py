from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet
from enderecos.views import EnderecoViewSet

# Configuração do roteador do DRF
router = DefaultRouter()
router.register(r'api/pacientes', PacienteViewSet)  # Rota para pacientes
router.register(r'api/enderecos', EnderecoViewSet)  # Rota para endereços

# Definição das rotas
urlpatterns = [
    path('admin/', admin.site.urls),  

    # Geração do esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Outras rotas
    path('', include(router.urls)),  # Rotas geradas automaticamente pelo roteador
]
