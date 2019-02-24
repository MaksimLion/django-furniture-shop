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

    title = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    option = models.CharField(max_length=20, choices=TYPES)

    def __str__(self):
        return self.title 


