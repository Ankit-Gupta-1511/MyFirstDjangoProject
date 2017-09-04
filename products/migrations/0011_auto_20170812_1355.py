# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170812_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Categories'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.SubCategories'),
        ),
    ]