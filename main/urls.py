from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('score/<int:pk>/addnum/', views.add_num, name='add_num'),
]