from datetime import datetime
from django.db import models
from monitoring.models import Sensor


class SensingData(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        to_field='serial_number',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(default=datetime.now)
    tempareture = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}_{self.timestamp.isoformat()}'
