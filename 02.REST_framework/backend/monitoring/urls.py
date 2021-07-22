from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from monitoring import views

urlpatterns = [
    path('sensor/', views.SensorList.as_view()),
    path('sensor/<slug:pk>', views.sensor.SensorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
