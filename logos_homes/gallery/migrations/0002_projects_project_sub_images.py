# Generated by Django 3.1 on 2020-09-10 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_sub_images',
            field=models.ImageField(default='', max_length=5, upload_to='images'),
        ),
    ]
