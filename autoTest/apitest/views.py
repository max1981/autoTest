#coding:utf8
import requests,urllib


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
    #登出
    auth.logout(request)
    return render(request, 'login.html')


@login_required
def apis_manager(request):
    #接口管理，获取当前用户，获取所有api接口
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

@login_required
def apisearch(request):
    username=request.session.get('user','')
    # search_apitestname = request.GET.get('apitestname','')
    search_apitestname = request.GET['apitestname']
    apisearch_list = Apis.objects.filter(apiName__icontains=search_apitestname)
    return render(request,'apis_manager.html',{"user":username,'apis':apisearch_list})

@login_required
def scenario_testing(request):
    username = request.session.get('user','')
    scenarios = Apitest.objects.all()
    return render(request,'scenario_testing.html',{'user':username,'scenarios':scenarios})

@login_required
def api_run(request,api_id):
    #执行接口测试
    username = request.session.get('user','')
    status = False
    api = Apis.objects.get(id=api_id)
    data = api.apiParamValue
    result = api.apiResult
    #用哪种提交方式get或者post
    if api.apiMethod  == '0':
        res = requests.get(api.apiUrl+urllib.urlencode(data))
    elif api.apiMethod == '1':
        data = eval(data)
        res = requests.post(api.apiUrl,data=data)
    else:
        res = None
    ###先判断是否有返回
    if res and result in res.text:
            #测试通过
        status = True
    else:
        print 'No res'
    api.apiStatus = True
    # api.apiStatus = status
    api.save()
    apisearch_list = Apis.objects.all()

    return render(request, 'apis_manager.html', {"user": username, 'apis': apisearch_list})




    # print data
    # return HttpResponse(content=data)