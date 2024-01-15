from rest_framework.viewsets import ModelViewSet

from maintenance.models import Status
from maintenance.serializers import StatusSerializer



class StatusViewset(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

