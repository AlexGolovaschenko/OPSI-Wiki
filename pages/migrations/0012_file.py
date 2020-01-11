# Generated by Django 3.0.1 on 2020-01-10 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20191226_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
                ('comment', models.CharField(blank=True, max_length=200, verbose_name='Комментарий')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]