from django.urls import path
from monitoring import views

urlpatterns = [
    path('sensor/', views.sensor.sensor_list),
    path('sensor/<slug:pk>', views.sensor.sensor_detail)
]
