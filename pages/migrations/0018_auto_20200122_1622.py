# Generated by Django 3.0.1 on 2020-01-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200122_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Программирование', 'Программирование'), ('Конструирование', 'Конструирование'), ('Управление проектами', 'Управление проектами'), ('Схемотехника', 'Схемотехника')], max_length=200, verbose_name='Название'),
        ),
    ]
