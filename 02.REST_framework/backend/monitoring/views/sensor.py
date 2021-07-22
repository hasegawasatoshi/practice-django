from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from monitoring.models.sensor import Sensor
from monitoring.serializers import SensorSerializer


class SensorList(APIView):
    def get(self, request, format=None):
        sensor = Sensor.objects.all()
        serializeer = SensorSerializer(sensor, many=True)
        return Response(serializeer.data)

    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDetail(APIView):
    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializeer = SensorSerializer(sensor)
        return Response(serializeer.data)

    def put(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sensor = self.get_object(pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
