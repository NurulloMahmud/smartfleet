from rest_framework import serializers
from fleet.models import Truck, TruckMake, TruckModel
from hiring.models import Driver
from hiring.serializers import DriverSerializer



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
    driver = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Truck
        fields = '__all__'


class TruckListSerializer(serializers.ModelSerializer):
    make = TruckMakeSerializer(read_only=True)
    model = TruckModelSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Truck
        fields = '__all__'