from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from fleet.models import Truck, TruckInUse
from fleet.serializers import (
    TruckCreateSerializer, TruckListSerializer,
    TruckInUseReadSerializer, TruckInUseWriteSerializer,
)



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
    

class TruckInUseViewSet(ModelViewSet):
    queryset = TruckInUse.objects.all()
    serializer_class = TruckInUseWriteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = TruckInUseReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TruckInUseReadSerializer(instance)
        return Response(serializer.data)