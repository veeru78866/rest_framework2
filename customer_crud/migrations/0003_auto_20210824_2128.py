# Generated by Django 2.2 on 2021-08-24 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_crud', '0002_auto_20210824_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercrudmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 21, 28, 27, 33238)),
        ),
    ]
