from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.api import viewsets

router = routers.DefaultRouter()
router.register(r'pontoturistico', viewsets.PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
