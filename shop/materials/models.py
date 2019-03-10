from django.db import models


class Kromka(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    photo = models.ImageField(blank=True, upload_to="materials/kromka/", verbose_name="Фотография")
    text = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кромка"
        verbose_name_plural = "Кромки"


class Leafs(models.Model):
    PHOTOPRINT = "photoprint"
    DEROCATE = "decorated"
    PESKOSTRYI = "sandblast"
    EKOKOZHA = "ekokozha"
    LAMINIROVANIE = "laminirovanie"

    OPTION = (
        (PHOTOPRINT, "Фотопечать"),
        (DEROCATE, "Декоративные перегородки"),
        (PESKOSTRYI,"Пескоструи"),
        (EKOKOZHA, "Экокожа"),
        (LAMINIROVANIE, "Ламинирование ДСП")
    )

    title = models.CharField(max_length=30, verbose_name="Название")
    photo = models.ImageField(blank=True, upload_to="materials/leafs/", verbose_name="Фотография")
    option = models.CharField(choices=OPTION, max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Створка"
        verbose_name_plural = "Створки"


class LDSP(models.Model):
    KRONOSPAN = "Kronospan"
    SWISSPAN = "Swisspan"
    SWISSPAN_NATUR = "Swisspan_natur"
    
    OPTION = (
        (KRONOSPAN, "KRONOSPAN"),
        (SWISSPAN, "SWISSPAN"),
        (SWISSPAN_NATUR, "SWISSPAN_NATUR"),
    )

    title = models.CharField(max_length=30, verbose_name="Название")
    option = models.CharField(max_length=50, verbose_name="Производитель", choices=OPTION)
    photo = models.ImageField(blank=True, upload_to="materials/LDSP/", verbose_name="Фотография")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ЛДСП"
        verbose_name_plural = "ЛДСП"


class FurnitureAccessories(models.Model):
    BLUM = "Blum"
    HETTICH = "Hettich"

    OPTION = (
        (BLUM, "BlUM"),
        (HETTICH, "HETTICH")
    )

    title = title = models.CharField(max_length=50, verbose_name="Название")
    photo = models.ImageField(blank=True, upload_to="materials/furniture_accessories/", verbose_name="Фотография")
    option = models.CharField(max_length=30, verbose_name="Производитель", choices=OPTION)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фурнитура"
        verbose_name_plural = "Фурнитура"