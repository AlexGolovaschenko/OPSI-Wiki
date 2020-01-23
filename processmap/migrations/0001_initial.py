# Generated by Django 3.0.1 on 2020-01-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0024_auto_20200123_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapAreaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_area', models.CharField(choices=[('01', 'Скрининг'), ('02', 'Сбор информации'), ('03', 'Анализ'), ('04', 'Исследование рынка'), ('05', 'Разработка концепции'), ('06', 'Выбор концепции'), ('07', 'Планирование'), ('08', 'Разработка прототипа'), ('09', 'ТЗ'), ('10', 'КД'), ('11', 'ПО'), ('12', 'Документация'), ('13', 'Сборка прототипа'), ('14', 'Подготовка производства'), ('15', 'Альфа-тестирование'), ('16', 'Бета-тестирование'), ('17', 'Создание продукта'), ('18', 'Разработка продукта'), ('19', 'Уточнение ТЗ'), ('20', 'Доработка КД'), ('21', 'Обеспечение производства'), ('22', 'Вывод на рынок и продажи'), ('23', 'Итерационная доработка'), ('24', 'Поддержка'), ('25', 'Вывод с рынка')], max_length=100, unique=True, verbose_name='Область рисунка')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
