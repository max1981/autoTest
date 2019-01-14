"""autoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apitest import views as apitest_views
from product import views as product_views
from bugManager import views as bug_views
from systemSet import views as sytemSet_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/',apitest_views.login,name='login'),
    url(r'^home/',apitest_views.home,name='home'),
    url(r'^logout/',apitest_views.logout,name='logout'),
    url(r'^product_manage/',product_views.product_manage,name='product_manage'),
    url(r'^apis_manage/',apitest_views.apis_manager,name='apis_manage'),
    url(r'^bug_manage/',bug_views.bug_manage,name='bug_manage'),
    url(r'^systemSet_manage/',sytemSet_views.systemSet_manage,name='systemSet_manage'),
    url(r'^user/',sytemSet_views.set_user,name='set_user'),
    url(r'^left/',apitest_views.left,name='left'),
    url(r'^apisearch/',apitest_views.apisearch,name='apisearch'),
    url(r'^scenario_testing/',apitest_views.scenario_testing,name='scenario_testing'),
    url(r'^api_run/(\d+)/$',apitest_views.api_run,name='api_run'),
]
