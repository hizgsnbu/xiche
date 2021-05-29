# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-28 07:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarWashLocalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=100, verbose_name='\u7f51\u70b9\u7f16\u53f7')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='\u540d\u79f0')),
                ('wifi_ssid', models.CharField(blank=True, max_length=100, verbose_name='wifi ID')),
                ('wifi_passwd', models.CharField(blank=True, max_length=100, verbose_name='wifi \u5bc6\u7801')),
                ('status', models.CharField(blank=True, max_length=100, verbose_name='\u7f51\u70b9\u72b6\u6001')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=300, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('mobile', models.CharField(blank=True, max_length=100, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('head', models.CharField(blank=True, max_length=300, verbose_name='\u5934\u50cf')),
                ('vcode', models.CharField(blank=True, max_length=300, verbose_name='\u9080\u8bf7\u7801')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8d26\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='UserCarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_no', models.CharField(blank=True, max_length=50, verbose_name='\u8f66\u724c\u53f7\u7801')),
                ('car_brand', models.CharField(blank=True, max_length=300, verbose_name='\u8f66\u8f86\u54c1\u724c')),
                ('car_model', models.CharField(blank=True, max_length=300, verbose_name='\u8f66\u8f86\u578b\u53f7')),
                ('car_buydate', models.CharField(blank=True, max_length=100, verbose_name='\u8d2d\u4e70\u65e5\u671f')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8d26\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='WashSessionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CarWashLocalModel', verbose_name='\u7f51\u70b9')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8d26\u53f7')),
            ],
        ),
    ]