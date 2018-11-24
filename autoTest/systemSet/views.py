# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from models import SystemSet

def systemSet_manage(request):
    userName = request.session.get('user','')
    systemSets = SystemSet.objects.all()
    return render(request,'systemSet_manage.html',{'user':userName,'systemSets':systemSets})

def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user','')
    return render(request,'set_users.html',{'user':username,'users':user_list})
