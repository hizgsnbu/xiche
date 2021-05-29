#encoding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HookModel(models.Model):
    method=models.CharField('method',max_length=500,blank=True)
    path=models.TextField(verbose_name='url',blank=True)
    head=models.TextField(verbose_name='head',blank=True)
    body=models.TextField(verbose_name='body',blank=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.method


class CustomerModel(models.Model):
    user=models.OneToOneField(User,verbose_name='账号')
    nick_name=models.CharField('用户昵称',max_length=300,blank=True)
    mobile=models.CharField('手机号码',max_length=100,blank=True)
    head = models.CharField('头像',max_length=300,blank=True)
    vcode=models.CharField('邀请码',max_length=300,blank=True) 

class UserCarModel(models.Model):
    user = models.ForeignKey(User,verbose_name='账号')
    car_no= models.CharField('车牌号码',max_length=50,blank=True)
    car_brand=models.CharField('车辆品牌',max_length=300,blank=True)
    car_model=models.CharField('车辆型号',max_length=300,blank=True)
    car_buydate=models.CharField('购买日期',max_length=100,blank=True)

class CarWashLocalModel(models.Model):
    no=models.CharField('网点编号',max_length=100,blank=True)
    name = models.CharField('名称',max_length=100,blank=True)
    wifi_ssid=models.CharField('wifi ID',max_length=100,blank=True)
    wifi_passwd=models.CharField('wifi 密码',max_length=100,blank=True)
    status=models.CharField('网点状态',max_length=100,blank=True)

class WashSessionModel(models.Model):
    user=models.ForeignKey(User,verbose_name='账号',blank=True)
    local=models.ForeignKey(CarWashLocalModel,verbose_name='网点',blank=True)
    start = models.DateTimeField(verbose_name='开始时间',blank=True,null=True)
    end=models.DateTimeField(verbose_name='结束时间',blank=True,null=True)
    

