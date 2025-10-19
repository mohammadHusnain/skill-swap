"""
URL configuration for api app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check_view, name='health_check'),
]
