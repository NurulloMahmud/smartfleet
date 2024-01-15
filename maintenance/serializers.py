from rest_framework import serializers
from maintenance.models import Status



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']

