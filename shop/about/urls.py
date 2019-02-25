from django.urls import path, include
from about import views


urlpatterns = [
    path('', views.about_us),
]
