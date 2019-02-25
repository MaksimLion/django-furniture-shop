from django.db import models


class Furniture(models.Model):

    TYPES = (
        ('kitchens','КУХНИ'),
        ('showcases','ВИТРИНЫ'),
        ('wardrobes','ШКАФЫ-КУПЕ'),
        ('offices','МЕБЕЛЬ ДЛЯ ОФИСА'),
        ('hallways','ПРИХОЖИЕ'),
        ('lounges','ГОСТИНЫЕ'),
        ('child','ДЕТСКИЕ'),
        ('closets','ГАРДЕРОБНЫЕ'),
        ('others','КРОВАТИ КОМОДЫ ТУМБЫ'),
    )

    title = models.CharField(max_length=20, verbose_name="Название")
    photo = models.ImageField(blank=True, verbose_name="Фото")
    option = models.CharField(max_length=20, choices=TYPES, verbose_name="Категория")
    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"

    def __str__(self):
        return self.title 


