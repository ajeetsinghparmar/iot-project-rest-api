from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'place', views.PlaceViewSet)
router.register(r'temperature', views.TemperatureViewSet)
router.register(r'humidity', views.HumidityViewSet)
router.register(r'pressure', views.PressureViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
