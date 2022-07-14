
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from localizacao.api.viewsets import LocalizacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]

