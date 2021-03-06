# Generated by Django 2.1.7 on 2019-03-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(default=0, max_length=30, verbose_name='Стоимость')),
                ('owner', models.CharField(max_length=30, verbose_name='Имя отправителя')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('status', models.CharField(choices=[('new', 'Новая заказ'), ('in_process', 'Заказ в процессе обработки'), ('renouncement', 'Заказ отклонен'), ('complete', 'Заказ выполнен '), ('?', 'Не получен ответ пользователя')], default='new', max_length=30, verbose_name='Статус')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
