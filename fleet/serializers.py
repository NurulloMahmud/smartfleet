from rest_framework import serializers
from fleet.models import Truck, TruckMake, TruckModel, TruckInUse
from hiring.models import Driver
from hiring.serializers import DriverCreateSerializer, DriverRetrieveSerializer



class TruckMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckMake
        fields = '__all__'


class TruckModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = '__all__'


class TruckCreateSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(
        queryset = TruckMake.objects.all(), required=False, allow_null=True
    )
    model = serializers.PrimaryKeyRelatedField(
        queryset = TruckModel.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Truck
        fields = '__all__'


class TruckListSerializer(serializers.ModelSerializer):
    make = TruckMakeSerializer(read_only=True)
    model = TruckModelSerializer(read_only=True)

    class Meta:
        model = Truck
        fields = '__all__'


class TruckInUseReadSerializer(serializers.ModelSerializer):
    drivers = DriverRetrieveSerializer(many=True)
    truck = TruckListSerializer()

    class Meta:
        model = TruckInUse
        fields = '__all__'


class TruckInUseWriteSerializer(serializers.ModelSerializer):
    drivers = serializers.PrimaryKeyRelatedField(
        queryset = Driver.objects.all(), many=True
    )

    truck = serializers.PrimaryKeyRelatedField(
        queryset = Truck.objects.all()
    )

    class Meta:
        model = TruckInUse
        fields = '__all__'