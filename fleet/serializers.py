from rest_framework import serializers
from fleet.models import Truck, TruckMake, TruckModel
from hiring.models import Driver



class TruckMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckMake
        fields = '__all__'


class TruckModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckModel
        fields = '__all__'


class TruckListCreateSerializer(serializers.ModelSerializer):
    make = TruckMakeSerializer(required=False, allow_null=True)
    model = TruckModelSerializer(required=False, allow_null=True)
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Truck
        fields = '__all__'


class TruckRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=TruckMake.objects.all(), allow_null=True, required=False)
    model = serializers.PrimaryKeyRelatedField(queryset=TruckModel.objects.all(), allow_null=True, required=False)
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Truck
        fields = '__all__'