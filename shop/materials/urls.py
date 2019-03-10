from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from materials import views

urlpatterns = [
    path('', views.materials),
    path('sandblast/', views.sandblast),
    path('photoprint/', views.photoprint),
    path('eco-leather/', views.eco_leather),
    path('lamination-dsp/', views.lamination_dsp),
    path('decorative-partitions/', views.decorative_partitions),
    path('kronospan/', views.kronospan),
    path('swisspan/', views.swisspan),
    path('swisspan-natur/', views.swisspan_natur),
    path('blum/', views.blum),
    path('hettich/', views.hettich)
]
