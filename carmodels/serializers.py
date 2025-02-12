from rest_framework import serializers
from .models import *

class CompactcarSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Compactcar
        fields='__all__'

class SedansSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Sedans
        fields='__all__'

class SuvSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Suv
        fields='__all__'

class VansSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Vans
        fields='__all__'

class TrucksSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Trucks
        fields='__all__'

class LuxurycarsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Luxurycars
        fields='__all__'

class ConvertiblesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Convertibles
        fields='__all__'

class Electriccars_HybridsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Electriccars_Hybrids
        fields='__all__'

class SportscarsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Sportscars
        fields='__all__'

class MotorcyclesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Motorcycles
        fields='__all__'