# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Jmeter(models.Model):
    jxmName = models.CharField('脚本名称',max_length=32)
    jxmPath = models.CharField('脚本路径',max_length=128)
    description = models.CharField('描述',max_length=256)
    result = models.CharField('结果',max_length=256)
    class Meta:
        verbose_name = '性能测试脚本'
        verbose_name_plural = '性能测试脚本'

    def __str__(self):
        return self.jxmName

