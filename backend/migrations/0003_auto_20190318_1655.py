# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_society_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
