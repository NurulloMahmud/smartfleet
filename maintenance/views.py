from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from maintenance.models import (
    Status, Case, Note, Odometer,
    Service, TruckService
)

from maintenance.serializers import (
    CaseWriteSerializer, StatusSerializer, 
    CaseReadSerializer, NoteSerializer,
    OdometerWriteSerializer, OdometerReadSerializer,
    ServiceSerializer, TruckServiceReadSerializer,
)

from fleet.models import Truck


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class StatusViewset(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class CaseListCreateView(APIView):
    def get(self, request):
        queryset = Case.objects.all()
        serializer = CaseReadSerializer(queryset, many=True)
        context = {
                "success": True,
                "message": "successfully created",
                "data": serializer.data,
            }

        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = CaseWriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            context = {
                "success": True,
                "message": "successfully created",
                "data": serializer.data,
            }

            return Response(context, status=status.HTTP_201_CREATED)
        
        context = {
            "success": False,
            "message": "invalid data"
        }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)


class CaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseWriteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class OdodmeterListCreateView(APIView):
    def get(self, request):
        queryset = Odometer.objects.all()
        serializer = OdometerReadSerializer(queryset, many=True)

        return Response({"Success": True, "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = OdometerWriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            context = {
                "success": True,
                "message": "successfully created",
                "data": serializer.data,
            }

            return Response(context, status=status.HTTP_201_CREATED)
        
        context = {
            "success": False,
            "message": "invalid data",
        }

        return Response(status=status.HTTP_400_BAD_REQUEST)


class OdodmeteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odometer.objects.all()
    serializer_class = OdometerWriteSerializer


class TruckServiceScheduleView(APIView):
    def get(self, request):
        queryset = TruckService.objects.all()
        serializer = TruckServiceReadSerializer(queryset, many=True)
        context = {
            "Success": True,
            "data": serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)
