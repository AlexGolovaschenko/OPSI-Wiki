# Generated by Django 3.0.1 on 2020-01-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20200120_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('SwDev', 'Программирование'), ('Const', 'Конструирование'), ('PrMan', 'Управление проектами'), ('CiEng', 'Схемотехника')], max_length=200, verbose_name='Название'),
        ),
    ]