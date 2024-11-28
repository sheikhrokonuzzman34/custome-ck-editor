from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.my_model_list, name='my_model_list'),
    path('create/', views.my_model_create, name='my_model_create'),
]