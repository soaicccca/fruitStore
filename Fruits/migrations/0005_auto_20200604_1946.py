# Generated by Django 3.0.6 on 2020-06-04 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fruits', '0004_auto_20200602_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='available',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
