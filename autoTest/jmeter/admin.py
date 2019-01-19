# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from jmeter.models import Jmeter



class JmeterAdmin(admin.ModelAdmin):
    list_display = ['id','jxmName','jxmPath','description','result']

admin.site.register(Jmeter)

# Register your models here.
