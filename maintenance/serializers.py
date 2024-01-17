from django.utils import timezone

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
