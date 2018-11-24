#-*- coding:utf-8 -*-
#Author:Max
#2018/10/11
from django.conf.urls import url
from django.conf.urls import include
from apitest import views as apiTestView

urlpatterns = [
    url('^login',apiTestView.login,name='login'),
]

