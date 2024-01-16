from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from maintenance.models import Status, Case, Note
from maintenance.serializers import (
    CaseWriteSerializer, StatusSerializer, 
    CaseReadSerializer, NoteSerializer
)



class StatusViewset(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class CaseListCreateView(APIView):
    def get(self, request):
        queryset = Case.objects.all()
        serializer = CaseReadSerializer(queryset, many=True)

        return Response({"Success": True , "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = CaseWriteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({"Success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({"Success": False}, status=status.HTTP_400_BAD_REQUEST)


class CaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseWriteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

