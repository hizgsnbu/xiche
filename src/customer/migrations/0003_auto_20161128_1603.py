# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-28 08:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_carwashlocalmodel_customermodel_usercarmodel_washsessionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washsessionmodel',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='washsessionmodel',
            name='local',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='customer.CarWashLocalModel', verbose_name='\u7f51\u70b9'),
        ),
        migrations.AlterField(
            model_name='washsessionmodel',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='washsessionmodel',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8d26\u53f7'),
        ),
    ]