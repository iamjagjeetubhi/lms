# Generated by Django 2.0.1 on 2018-06-16 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0015_auto_20180616_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='value',
        ),
    ]
