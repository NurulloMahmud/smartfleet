from rest_framework.response import Response
from rest_framework import generics
from hiring.serializers import DriverCreateSerializer, DriverRetrieveSerializer
from hiring.models import Driver



class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        list_serializer = DriverRetrieveSerializer(queryset, many=True)

        return Response(list_serializer.data)


class DriverRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        custom_serializer = DriverRetrieveSerializer(instance)

        return Response(custom_serializer.data)

