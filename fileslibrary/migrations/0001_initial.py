# Generated by Django 3.0.1 on 2020-01-28 09:58

from django.db import migrations, models
import django.db.models.deletion
import fileslibrary.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=fileslibrary.models.file_storage_path, verbose_name='Файл')),
                ('alter_name', models.CharField(blank=True, max_length=200, verbose_name='Переименовать файл')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileslibrary.Topic', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
