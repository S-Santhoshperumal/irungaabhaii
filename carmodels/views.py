from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class CompactcarViewSet(viewsets.ModelViewSet):
    queryset = Compactcar.objects.all()
    serializer_class = CompactcarSerializer
    parser_classes = (MultiPartParser, FormParser)


class SedansViewSet(viewsets.ModelViewSet):
    queryset = Sedans.objects.all()
    serializer_class = SedansSerializer
    parser_classes = (MultiPartParser, FormParser)

class SuvViewSet(viewsets.ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    parser_classes = (MultiPartParser, FormParser)

class  VansViewSet(viewsets.ModelViewSet):
    queryset =  Vans.objects.all()
    serializer_class = VansSerializer
    parser_classes = (MultiPartParser, FormParser)

class TrucksViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.all()
    serializer_class = TrucksSerializer
    parser_classes = (MultiPartParser, FormParser)

class LuxurycarsViewSet(viewsets.ModelViewSet):
    queryset = Luxurycars.objects.all()
    serializer_class = LuxurycarsSerializer
    parser_classes = (MultiPartParser, FormParser)

class ConvertiblesViewSet(viewsets.ModelViewSet):
    queryset = Convertibles.objects.all()
    serializer_class = ConvertiblesSerializer
    parser_classes = (MultiPartParser, FormParser)

class Electriccars_HybridsViewSet(viewsets.ModelViewSet):
    queryset =  Electriccars_Hybrids.objects.all()
    serializer_class = Electriccars_HybridsSerializer
    parser_classes = (MultiPartParser, FormParser)

class SportscarsViewSet(viewsets.ModelViewSet):
    queryset = Sportscars.objects.all()
    serializer_class = SportscarsSerializer
    parser_classes = (MultiPartParser, FormParser)

class MotorcyclesViewSet(viewsets.ModelViewSet):
    queryset =  Motorcycles.objects.all()
    serializer_class = MotorcyclesSerializer
    parser_classes = (MultiPartParser, FormParser)

