from django.db import models

class Sale(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Скидки"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return self.title

    