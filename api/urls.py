from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_func, name='api_test'),
]