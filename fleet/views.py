from rest_framework import generics
from fleet.models import Truck
from fleet.serializers import TruckListCreateSerializer, TruckRetrieveUpdateDeleteSerializer


class TruckListCreateAPIView(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckListCreateSerializer


class TruckRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckRetrieveUpdateDeleteSerializer
