# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from systemSet.models import SystemSet
class SystemSetAdmin(admin.ModelAdmin):
    list_display = [SystemSet.urlName,SystemSet.systemUrl]

admin.site.register(SystemSet)
