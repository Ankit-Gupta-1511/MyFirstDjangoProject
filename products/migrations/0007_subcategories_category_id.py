# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_subcategories_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Categories'),
        ),
    ]
