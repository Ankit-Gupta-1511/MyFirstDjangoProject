# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndUsers',
            fields=[
                ('user_id', models.CharField(default='U_test', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(default='U_Name', max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]