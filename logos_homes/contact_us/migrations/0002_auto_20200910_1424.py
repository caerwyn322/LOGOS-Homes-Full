# Generated by Django 3.1 on 2020-09-10 02:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='sent_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 10, 14, 24, 47, 305853)),
        ),
    ]
