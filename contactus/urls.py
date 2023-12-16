from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('contact_success/', views.contact_success, name='contact_success'),
]