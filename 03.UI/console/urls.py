from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.IndexView.as_view(), name='index'),
    path('data/', views.get_data),
    path('login/', auth_views.LoginView.as_view(template_name='console/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='console/logout.html'), name='logout'),
]
