from django.contrib import admin
from product.models import Product

import sys;

reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']

admin.site.register(Product)

