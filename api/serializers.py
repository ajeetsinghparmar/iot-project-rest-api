from .models import Place, Temperature, Humidity, Pressure
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Temperature
        fields = '__all__'

    def create(self, validated_data):
        place_data = validated_data.pop('place')
        place = Place.objects.get_or_create(**place_data)
        temperature = Temperature.objects.create(place=place[0],**validated_data)
        return temperature

class HumiditySerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Humidity
        fields = '__all__'

    def create(self, validated_data):
        place_data = validated_data.pop('place')
        place = Place.objects.get_or_create(**place_data)
        humidity = Humidity.objects.create(place=place[0],**validated_data)
        return humidity

class PressureSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Pressure
        fields = '__all__'

    def create(self, validated_data):
        place_data = validated_data.pop('place')
        place = Place.objects.get_or_create(**place_data)
        pressure = Pressure.objects.create(place=place[0],**validated_data)
        return pressure
