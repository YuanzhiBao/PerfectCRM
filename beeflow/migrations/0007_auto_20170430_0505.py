# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-30 05:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beeflow', '0006_flow_in_queue'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowrole',
            name='is_dynamic_role',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='flowrole',
            name='role_lookup_func',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='查找动态role的函数'),
        ),
        migrations.AlterField(
            model_name='flowrole',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
