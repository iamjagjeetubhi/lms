# Generated by Django 2.0.1 on 2018-06-15 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_auto_20180615_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 15, 17, 52, 31, 256454, tzinfo=utc), max_length=12, null=True),
        ),
    ]
