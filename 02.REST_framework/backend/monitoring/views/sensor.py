from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from monitoring.models.sensor import Sensor
from monitoring.serializers import SensorSerializer


@csrf_exempt
def sensor_list(request):
    if request.method == 'GET':
        sensor = Sensor.objects.all()
        serializeer = SensorSerializer(sensor, many=True)
        return JsonResponse(serializeer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SensorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def sensor_detail(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SensorSerializer(sensor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.erros, status=400)

    elif request.method == 'DELETE':
        sensor.delete()
        return HttpResponse(status=204)
