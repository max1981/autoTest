# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from jmeter.models import Jmeter



@login_required
def showAllJxm(request):
    jxms = Jmeter.objects.all()

    return render(request,'all_jxm.html',{'jxms':jxms})

def showResult(request):
    return render(request,'http://127.0.0.1:8080/output/')

# Create your views here.
