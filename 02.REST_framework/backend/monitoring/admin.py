from django.contrib import admin
from monitoring.models import Sensor
from monitoring.models import SensingData

admin.site.register(Sensor)
admin.site.register(SensingData)
