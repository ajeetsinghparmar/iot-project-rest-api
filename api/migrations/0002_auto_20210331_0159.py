# Generated by Django 3.1.2 on 2021-03-31 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]