# Generated by Django 2.0 on 2021-04-17 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 17, 14, 28, 41, 147463, tzinfo=utc)),
        ),
    ]
