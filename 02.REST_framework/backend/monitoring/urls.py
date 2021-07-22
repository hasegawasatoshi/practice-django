from django.urls import path, include
from rest_framework.routers import DefaultRouter
from monitoring import views

sensor_list = views.sensor.SensorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

sensor_detail = views.sensor.SensorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'sensor', views.sensor.SensorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
