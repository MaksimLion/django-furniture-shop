from django.urls import path, include
from sales import views

urlpatterns = [
    path('', views.sales)
]