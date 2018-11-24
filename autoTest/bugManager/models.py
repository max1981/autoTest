#coding:utf8
from __future__ import unicode_literals

from django.db import models
from product.models import Product

class BugManager(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    bugName = models.CharField('bug名称',max_length=128)
    bugDetail = models.CharField('bug详情',max_length=256)
    BUG_STATUS = (('激活','激活'),('已解决','已解决'),('关闭','关闭'))
    bugStatus = models.CharField(verbose_name='bug状态',choices=BUG_STATUS,default='激活',max_length=32,null=True)
    BUG_LEVEL = (('1','1'),('2','2'),('3','3'))
    bugLevel = models.CharField(verbose_name='bug等级',choices=BUG_LEVEL,default='3',max_length=32,null=True)
    bugCreate = models.CharField('bug创建者',max_length=32)
    bugAssign = models.CharField('bug分配给',max_length=32)
    bugCreateTime = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = 'Bug管理'
        verbose_name_plural = 'Bug管理'
    def __str__(self):
        return self.bugName



# Create your models here.
