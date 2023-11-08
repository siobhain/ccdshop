# from django.contrib import admin
from django.urls import path
from . import views
from .views import handler404

urlpatterns = [
    path('', views.index, name='home')
]
handler404 = 'home.views.handler404'
