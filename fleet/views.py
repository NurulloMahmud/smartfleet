from rest_framework import generics, status
from rest_framework.response import Response

from fleet.models import Truck
from fleet.serializers import TruckCreateSerializer, TruckListSerializer



class TruckListCreateAPIView(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        custom_serializer = TruckListSerializer(queryset, many=True)
        
        return Response(custom_serializer.data)



class TruckRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TruckListSerializer(instance)  # Serialize the instance

        return Response(serializer.data)
