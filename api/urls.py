from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.get_all_categories, name='categories'),
]
