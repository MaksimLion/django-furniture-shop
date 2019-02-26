from django.db import models

# Create your models here.
class Order(models.Model):
    NEW = "new"
    IN_PROCESS = "in_process"
    RENOUNCEMENT = "renouncement"
    COMPLETE = "complete"
    WITH_QUESTION = "?"

    STATUSES = (
        (NEW, "Новая заказ"),
        (IN_PROCESS, "Заказ в процессе обработки"),
        (RENOUNCEMENT, "Заказ отклонен"),
        (COMPLETE, "Заказ выполнен "),
        (WITH_QUESTION, "Не получен ответ пользователя")
    )

    cost = models.CharField(max_length=30, verbose_name="Стоимость", default=0)
    owner = models.CharField(max_length=30, verbose_name="Заказчик")
    phone = models.CharField(max_length=10, verbose_name="Телефон")
    status = models.CharField(max_length=30, verbose_name="Статус", choices=STATUSES, default=NEW)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


    def __str__(self):
        return self.owner