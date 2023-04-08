from django.urls import path
from . import views

urlpatterns = [
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('loyalty_dashboard/', views.loyalty_dashboard, name='loyalty_dashboard'),
    path('map/', views.map, name='map'),
]