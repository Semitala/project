# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-07-23 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200723_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]