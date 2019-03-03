from django.contrib import admin
from .models import LDSP, Leafs, Kromka, FurnitureAccessories

admin.site.register(FurnitureAccessories)
admin.site.register(LDSP)
admin.site.register(Kromka)
admin.site.register(Leafs)