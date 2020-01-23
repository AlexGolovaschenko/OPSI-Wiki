# Generated by Django 3.0.1 on 2020-01-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_auto_20200122_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[(None, '---------'), ('SOFT_DEV', 'Программирование'), ('CONSTRUCT', 'Конструирование'), ('PROJ_MANAG', 'Управление проектами'), ('CIRC_ENG', 'Схемотехника')], max_length=20, unique=True, verbose_name='Название'),
        ),
    ]