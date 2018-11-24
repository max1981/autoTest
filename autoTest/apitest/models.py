#coding:utf8
from __future__ import unicode_literals

from django.db import models
from product.models import Product

class Apitest(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    apiTestName = models.CharField('流程接口名称',max_length=64)
    apiTestDesc = models.CharField('流程接口描述',max_length=128,null=True)
    apiTester = models.CharField('测试负责人',max_length=32)
    apiTestResult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'


    def __str__(self):
        return self.apiTestName

class ApiStep(models.Model):
    ApiTest = models.ForeignKey(Apitest,on_delete=models.CASCADE,)
    apiName = models.CharField('接口名称',max_length=128)
    apiUrl = models.CharField('接口地址',max_length=128)
    apiParamValue = models.CharField('参数和值',max_length=128)
    RUQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    apiMethod = models.CharField(verbose_name='请求方法',choices=RUQUEST_METHOD,default='get',max_length=256,null=True)
    apiResult =models.CharField('预期结果',max_length=256)
    apiStatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间',auto_now=True)


    def __str__(self):
        return self.apiName


class Apis(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,)
    apiName = models.CharField('接口名称', max_length=128)
    apiUrl = models.CharField('接口地址', max_length=128)
    apiParamValue = models.CharField('参数和值', max_length=128)
    RUQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    apiMethod = models.CharField(verbose_name='请求方法', choices=RUQUEST_METHOD, default='0', max_length=256, null=True)
    apiResult = models.CharField('预期结果', max_length=256)
    apiStatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '单一场景接口测试'
        verbose_name_plural = '单一场景接口测试'

    def __str__(self):
        return self.apiName


