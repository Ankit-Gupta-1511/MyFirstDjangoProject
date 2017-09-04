# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20, unique=True)),
                ('product_price', models.IntegerField(default=100)),
                ('product_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieces_left', models.IntegerField(default=0)),
                ('pieces_sold', models.IntegerField(default=0)),
                ('pieces_ordered', models.IntegerField(default=0)),
                ('total_pieces', models.IntegerField(default=0)),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]