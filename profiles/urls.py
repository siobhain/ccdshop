from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
        ),
    path('subscribed_users_list/', views.subscribed_users_list, name='subscribed_users_list'),
]
