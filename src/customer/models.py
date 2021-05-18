from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HookModel(models.Model):
    method=models.CharField('method',max_length=500,blank=True)
    path=models.TextField(verbose_name='url',blank=True)
    head=models.TextField(verbose_name='head',blank=True)
    body=models.TextField(verbose_name='body',blank=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.method
