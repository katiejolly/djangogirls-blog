# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170912_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='blog\\images\\code.png', upload_to='blog/images'),
        ),
    ]
