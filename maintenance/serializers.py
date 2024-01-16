from rest_framework import serializers
from maintenance.models import Status, Case, Note, Odometer

from fleet.models import Truck
from fleet.serializers import TruckListSerializer




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']


class CaseWriteSerializer(serializers.ModelSerializer):
    truck = serializers.PrimaryKeyRelatedField(
        queryset = Truck.objects.all()
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset = Status.objects.all()
    )

    class Meta:
        model = Case
        fields = '__all__'


class CaseReadSerializer(serializers.ModelSerializer):
    truck = TruckListSerializer()
    status = StatusSerializer()

    class Meta:
        model = Case
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class OdodmeterReadSerializer(serializers.ModelSerializer):
    truck = TruckListSerializer()

    class Meta:
        model = Odometer
        fields = '__all__'


class OdometerWriteSerializer(serializers.ModelSerializer):
    truck = serializers.PrimaryKeyRelatedField(
        queryset = Truck.objects.all()
    )

    class Meta:
        model = Odometer
        fields = '__all__'

