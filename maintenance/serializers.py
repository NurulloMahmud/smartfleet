from django.utils import timezone

from rest_framework import serializers
from maintenance.models import (
    Status, Case, 
    Note, Odometer,
    Service, TruckService,
)

from fleet.models import Truck
from fleet.serializers import TruckListSerializer

from datetime import date, timedelta




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


class OdometerReadSerializer(serializers.ModelSerializer):
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

    def validate(self, data):
        """
        validate incoming value for ododmeter
        1 - incoming value cannot be less than 0
        2 - incoming value for odometer cannot be less than latest odometer value
        3 - do not record the odometer value if it is more than 10k compared to last week's
        """
        truck_id = data.get('truck')
        current_odometer = data.get('odometer')

        # validate truck instance
        try:
            truck_instance = Truck.objects.get(id=truck_id)
        except Truck.DoesNotExist:
            raise serializers.ValidationError("Truck does not exist")

        # validate current odometer
        if current_odometer < 0:
            raise serializers.ValidationError("odometer cannot be in negative")

        # if this is the first odometer record for truck instance, complete the validation
        if not Odometer.objects.filter(truck=truck_instance).exists():
            return data

        # Get the last odometer instance, if it exists
        last_odometer_instance = Odometer.objects.filter(truck=truck_instance).order_by('-date').first()
        
        if last_odometer_instance:
            last_odometer = last_odometer_instance.odometer
            last_week = timezone.now().date() - timedelta(days=7)

            # Validate the 10k mileage difference within the last week
            if last_odometer_instance.date >= last_week and last_odometer + 10000 < current_odometer:
                raise serializers.ValidationError("Mileage difference is suspicious.")

            # Odometer reading cannot decrease over time
            if current_odometer < last_odometer:
                raise serializers.ValidationError("Odometer reading cannot decrease from the previous reading.")

        return data


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TruckServiceReadSerializer(serializers.ModelSerializer):
    truck = TruckListSerializer()
    service = ServiceSerializer()
    mile_since_last_service = serializers.SerializerMethodField()
    days_since_last_service = serializers.SerializerMethodField()

    class Meta:
        model = TruckService
        fields = '__all__'
    
    # calculate days since last service
    def get_days_since_last_service(self, obj):
        today = date.today()

        if obj.last_service_date:
            return (today - obj.last_service_date).days()
        
        return None

    # calculate the miles since the last service
    def get_mile_since_last_service(self, obj):
        current_odometer = Odometer.objects.filter(truck=obj.truck).order_by('-date').values('odometer', ).first()
        if obj.mile_since_last_service:
            return current_odometer - obj.last_service_milage

        return None


class TruckServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckService
        fields = '__all__'
    
    # check if truck with this service record exists
    def create(self, validated_data):
        try:
            truck_instance = Truck.objects.get(id=validated_data.get('truck'))
            service_instance = Service.objects.get(id=validated_data.get('service'))
        except (Truck.DoesNotExist, Service.DoesNotExist):
            raise serializers.ValidationError("Invalid data for truck or service")
          
        if TruckService.objects.filter(truck=truck_instance, service=service_instance).exists():
            raise serializers.ValidationError("This service for this truck already exists, try updating the record instead")
        
        instance = TruckService.objects.create(**validated_data)

        return instance

