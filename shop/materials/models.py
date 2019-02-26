from django.db import models


# class DSP(models.Model):
#     KRONOSPAN = "KRONOSPAN"
#     SWISSPAN = "SWISPAN"
#     SWISSPAN_NATUR = "SWISPAN_NATUR" 
#     BRANDS = (
#         (KRONOSPAN, "KRONOSPAN"),
#         (SWISSPAN, "SWISPAN"),
#         (SWISSPAN_NATUR, "SWISPAN NATUR"),
#     )

#     title = models.CharField(max_length=20, verbose_name="Название")
#     description = models.TextField(verbose_name="Описание")
#     brand = models.CharField(choices=BRANDS, max_length="Бренд")

#     def __str__(self):
#         return self.title


# class Sash(models.Model):
#     SENATOR_SYSTEM = "SYNATER_SYSTEM"
#     HETTICH_SYSTEM = "SYSTEM_HETTICH"
#     SASH_SEPARATION = "SASH_SEPARATION"
#     SASH_DEVICE = "SASH_DEVICE"
    
#     CATEGORIES = (
#         (SENATOR_SYSTEM, "Система SENATOR"),
#         (HETTICH_SYSTEM, "Система HETTICH"),
#         (SASH_SEPARATION, "Разделение створок")
#         (SASH_DEVICE, "Устройство створки")
#     )

#     option = models.CharField(choices=CATEGORIES, max_length=30)
#     photo = models.ImageField(blank=True)

    

    