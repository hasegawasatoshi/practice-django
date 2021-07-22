from rest_framework import serializers
from monitoring.models import Sensor, SensingData


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['serial_number', 'display_name', 'created_at', 'updated_at']


class SensingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensingData
        fields = ['sensor', 'timestamp',
                  'tempareture', 'humidity', 'created_at']
