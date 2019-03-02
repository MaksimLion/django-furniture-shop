# Generated by Django 2.1.7 on 2019-03-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureAccessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='materials/furniture_accessories/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Фурнитура',
                'verbose_name_plural': 'Фурнитура',
            },
        ),
        migrations.CreateModel(
            name='Kromka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='materials/kromka/', verbose_name='Фотография')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Кромка',
                'verbose_name_plural': 'Кромки',
            },
        ),
        migrations.CreateModel(
            name='LDSP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('option', models.CharField(choices=[('Kronospan', 'KRONOSPAN'), ('Swisspan', 'SWISSPAN'), ('Swisspan_natur', 'SWISSPAN_NATUR')], max_length=50, verbose_name='Производитель')),
                ('photo', models.ImageField(blank=True, upload_to='materials/LDSP/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'ЛДСП',
                'verbose_name_plural': 'ЛДСП',
            },
        ),
        migrations.CreateModel(
            name='Leafs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='materials/leafs/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Створка',
                'verbose_name_plural': 'Створки',
            },
        ),
    ]
