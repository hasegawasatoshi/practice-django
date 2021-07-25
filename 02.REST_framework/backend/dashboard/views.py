from django.shortcuts import render
from monitoring.models import Sensor
from monitoring.serializers import SensorSerializer

import json


def sensor_list(request):
    if request.method == 'GET':
        sensor = Sensor.objects.all()
        serializer = SensorSerializer(sensor, many=True)
        print(serializer.data)
        content = {'sensor_list': json.loads(json.dumps(serializer.data))}
        return render(request, 'dashboard/sensor_list.html', content)
