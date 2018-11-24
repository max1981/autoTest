from django.contrib import admin
from bugManager.models import BugManager


# Register your models here.
class BugManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'bugName', 'bugDetail', 'bugCreate', 'bugStatus', 'bugAssign', 'bugLevel', 'bugCreateTime']

admin.site.register(BugManager)
