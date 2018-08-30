from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', views.post_list, name='post_list'),
]