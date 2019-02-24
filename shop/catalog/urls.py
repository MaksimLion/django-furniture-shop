from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog import views


urlpatterns = [
    path('', views.main),
    path('categories', views.categories)
]
