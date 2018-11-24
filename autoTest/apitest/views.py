#coding:utf8
import requests


from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from apitest.models import Apis, ApiStep, Apitest


# Create your views here.

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


@login_required
def apis_manager(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, 'apis_manager.html', {'user': username, 'apis': apis_list})


def checkApi(request,id):
    testApi = Apis.objects.get(id=id)
    url = testApi['apiUrl']
    apiParamValue = testApi['apiParamValue']
    data = requests.get(url,params=apiParamValue)

    return render(request,'api_result.html',{})

def left(request):
    return render(request,'left.html')

def myTest(request):
    return render(request,'newTest.html')

@login_required
def apisearch(request):
    username=request.session.get('user','')
    # search_apitestname = request.GET.get('apitestname','')
    search_apitestname = request.GET['apitestname']
    apisearch_list = Apis.objects.filter(apiName__icontains=search_apitestname)
    return render(request,'apis_manager.html',{"user":username,'apis':apisearch_list})