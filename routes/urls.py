
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router =DefaultRouter()
router.register("location",LocationView)
router.register("vehicle",VehicleView)
urlpatterns = [
path('',include(router.urls))
]
