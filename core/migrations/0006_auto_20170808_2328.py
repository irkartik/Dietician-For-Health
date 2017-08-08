# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopAdBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_text', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=10000)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Ad Bar Section',
                'verbose_name_plural': 'Ad Bar Section',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Video'},
        ),
    ]
