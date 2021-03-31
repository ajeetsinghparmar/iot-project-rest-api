from .models import Place, Temperature, Humidity, Pressure
from rest_framework import viewsets, permissions
from api.serializers import PlaceSerializer, TemperatureSerializer, HumiditySerializer, PressureSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows places to be viewed or Added
    '''
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]

class TemperatureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Temperatures to be viewed or Added
    '''
    queryset = Temperature.objects.all().order_by('-date')
    serializer_class = TemperatureSerializer
    permission_classes = [permissions.AllowAny]

class HumidityViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Humidity to be viewed or Added
    '''
    queryset = Humidity.objects.all().order_by('-date')
    serializer_class = HumiditySerializer
    permission_classes = [permissions.AllowAny]

class PressureViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Pressure to be viewed or Added
    '''
    queryset = Pressure.objects.all().order_by('-date')
    serializer_class = PressureSerializer
    permission_classes = [permissions.AllowAny]
