from django.shortcuts import render

from travl.models import Facility, Location
from rest_framework import generics
from .serializers import FacilitySerializer, LocationSerializer, UserSerializer
# Create your views here.


class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = UserSerializer
