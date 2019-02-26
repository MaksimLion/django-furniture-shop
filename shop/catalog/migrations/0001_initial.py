# Generated by Django 2.1.5 on 2019-02-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='categories/', verbose_name='Фото')),
                ('option', models.CharField(choices=[('kitchens', 'КУХНИ'), ('showcases', 'ВИТРИНЫ'), ('wardrobes', 'ШКАФЫ-КУПЕ'), ('offices', 'МЕБЕЛЬ ДЛЯ ОФИСА'), ('hallways', 'ПРИХОЖИЕ'), ('lounges', 'ГОСТИНЫЕ'), ('child', 'ДЕТСКИЕ'), ('closets', 'ГАРДЕРОБНЫЕ'), ('others', 'КРОВАТИ КОМОДЫ ТУМБЫ')], max_length=20, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Мебель',
                'verbose_name_plural': 'Мебель',
            },
        ),
    ]
