from rest_framework import serializers
from hiring.models import Driver
from management.models import Company
from fleet.models import Truck
from management.serializers import CompanySerializer



class DriverCreateSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset = Company.objects.all(), 
        required=False, allow_null=True
    )
    
    truck = serializers.PrimaryKeyRelatedField(
        queryset = Truck.objects.all(),
        required=False, allow_null=True
    )

    class Meta:
        model = Driver
        fields = '__all__'


class DriverRetrieveSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'

