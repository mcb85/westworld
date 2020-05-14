# Generated by Django 3.0.5 on 2020-05-06 00:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 0, 49, 23, 788315, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 0, 49, 23, 788315, tzinfo=utc)),
        ),
    ]
