# Generated by Django 3.0.1 on 2019-12-26 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20191226_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='icon',
        ),
    ]