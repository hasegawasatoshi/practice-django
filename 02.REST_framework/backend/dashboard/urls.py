from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'sensor_list', views.sensor_list, name='sensor_list'),
]
