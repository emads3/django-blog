# Generated by Django 3.0.3 on 2020-02-27 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0002_auto_20200227_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 52, 18, 776676, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 52, 18, 775657, tzinfo=utc)),
        ),
    ]