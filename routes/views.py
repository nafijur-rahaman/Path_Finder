from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# Create your views here.

class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class=LocationSerializer


# filtering process
class VehicleFilter(filters.FilterSet):
    start_location_name = filters.CharFilter(method='filter_start_location')
    end_location_name = filters.CharFilter(method='filter_end_location')

    class Meta:
        model = Vehicle
        fields = ['start_location_name', 'end_location_name']

    def filter_start_location(self, queryset, name, value):
      
        start_location = get_object_or_404(Location, name=value)
        return queryset.filter(start_location=start_location)

    def filter_end_location(self, queryset, name, value):
  
        end_location = get_object_or_404(Location, name=value)
        return queryset.filter(end_location=end_location)

class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class=VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter

    