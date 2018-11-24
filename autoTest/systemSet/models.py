# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class SystemSet(models.Model):
    urlName = models.CharField('环境名称',max_length=32)
    systemUrl = models.CharField('url',max_length=128)

    class Meta:
        verbose_name = '系统设置'
        verbose_name_plural = '系统设置'


    def __str__(self):
        return self.urlName
