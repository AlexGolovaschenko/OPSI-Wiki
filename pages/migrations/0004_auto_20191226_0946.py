# Generated by Django 3.0.1 on 2019-12-26 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191224_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('icon', models.ImageField(default='topic_icon_default.png', upload_to='topic_icons')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок отображения')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.TextField(blank=True, verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='section',
            name='headline',
            field=models.CharField(blank=True, max_length=200, verbose_name='Оглавление'),
        ),

    ]