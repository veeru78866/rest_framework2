# Generated by Django 2.2 on 2021-08-24 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerMVSModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('room_number', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 8, 24, 23, 5, 25, 285733))),
            ],
        ),
    ]
