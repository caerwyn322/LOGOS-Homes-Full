# Generated by Django 3.1 on 2020-09-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(default='', max_length=50)),
                ('design_price', models.IntegerField()),
                ('design_desc', models.TextField(default='')),
                ('design_specs', models.FileField(upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Designs',
            },
        ),
    ]
