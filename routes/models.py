from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=120,unique=True)
    
    
    def __str__(self):
        return self.name
    

class Vehicle(models.Model):
    start_location =models.OneToOneField("Location",on_delete=models.CASCADE, related_name='start_location_here')
    end_location =models.OneToOneField("Location", on_delete=models.CASCADE, related_name="end_location_here")
    vehicle_name =models.CharField(max_length=120)
    vehicle_type=models.CharField(max_length=50, choices=[('bus','bus'),('leguna','leguna')])
    fare=models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.start_location} --->{self.end_location} : {self.vehicle_name}"
    

    

    
    
    
