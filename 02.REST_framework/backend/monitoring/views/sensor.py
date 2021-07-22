from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework import viewsets
from monitoring.models.sensor import Sensor
from monitoring.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
