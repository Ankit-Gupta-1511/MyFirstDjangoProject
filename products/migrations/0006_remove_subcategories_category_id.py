# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170812_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategories',
            name='category_id',
        ),
    ]
