from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from catalog import views


urlpatterns = [
    path('', views.categories),
    path('kitchens', views.kitchens, name='kitchens'),
    path('wardrobes', views.wardrobes),
    path('showcases', views.showcases),
    path('lounges', views.lounges),
    path('offices', views.offices),
    path('closets', views.closets),
    path('hallways', views.hallways),
    path('child', views.child),
    path('others', views.others),
]
