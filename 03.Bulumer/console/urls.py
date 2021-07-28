from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.IndexView.as_view(), name='index'),
    path('data/', views.get_data)
]
