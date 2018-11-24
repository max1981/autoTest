from django.contrib import admin
from apitest.models import Apitest,ApiStep,Apis


class ApiStepAdmin(admin.TabularInline):
    list_display = ['id','apiName','apiUrl','apiParamvalue','apiMethod','apiResult','apiStatus','create_time','apiTest']
    model = ApiStep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['id','apiTestName','apiTester','apiTestResult','create_time']
    inlines = [ApiStepAdmin]


class ApisAdmin(admin.ModelAdmin):
    list_display = ['id', 'apiName', 'apiUrl', 'apiParamvalue', 'apiMethod', 'apiResult', 'apiStatus', 'create_time', 'apiTest']


admin.site.register(Apis)
admin.site.register(Apitest,ApitestAdmin)