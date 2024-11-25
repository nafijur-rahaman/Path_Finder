from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    location_name=serializers.SerializerMethodField()
    class Meta:
        model = Location
        fields ="__all__"
    
    def get_location_name(self,obj):
        return obj.name
        
class VehicleSerializer(serializers.ModelSerializer):
    start_location_name=serializers.SerializerMethodField()
    end_location_name=serializers.SerializerMethodField()
    class Meta:
        model=Vehicle
        fields="__all__"
        
    def get_start_location_name(self,obj):
        return obj.start_location.name
    def get_end_location_name(self,obj):
        return obj.end_location.name


