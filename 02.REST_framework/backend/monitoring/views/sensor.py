from datetime import datetime, timezone, timedelta
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# from monitoring.models.sensor import Sensor
from monitoring.models import Sensor, SensingData
from monitoring.serializers import SensorSerializer, SensingDataSerializer

JST = timezone(timedelta(hours=+9), 'JST')


def now():
    return int(datetime.now(timezone.utc).strftime('%s'))


def epoch_to_iso_jst(epoch):
    try:
        v = int(epoch)
    except Exception:
        v = now()
    return datetime.fromtimestamp(v).replace(tzinfo=timezone.utc).astimezone(tz=JST).isoformat()


def search_data(request, pk):
    try:
        sensor = Sensor.objects.get(pk=pk)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        from_dt = int(request.GET.get('from'))
    except Exception:
        from_dt = now() - 3600
    finally:
        from_dt = epoch_to_iso_jst(from_dt)

    try:
        to_dt = int(request.GET.get('to'))
    except Exception:
        to_dt = now()
    finally:
        to_dt = epoch_to_iso_jst(to_dt)

    data = SensingData.objects.filter(
        sensor=sensor, timestamp__gte=from_dt, timestamp__lte=to_dt)
    serializer = SensingDataSerializer(data, many=True)
    return Response(serializer.data)


def post_data(request, pk):
    data = request.data
    data['sensor'] = pk
    if 'timestamp' not in data:
        data['timestamp'] = datetime.now().astimezone(tz=JST).isoformat()

    serializer = SensingDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @ action(detail=True, methods=['GET', 'POST'])
    def data(self, request, *args, **kwargs):
        if request.method == 'GET':
            return search_data(request, kwargs['pk'])

        elif request.method == 'POST':
            return post_data(request, kwargs['pk'])

        return Response({}, status=status.HTTP_400_BAD_REQUEST)
