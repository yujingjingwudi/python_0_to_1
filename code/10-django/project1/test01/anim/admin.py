from django.contrib import admin

from .models import WifeInfo,ProductionInfo
# Register your models here.



class WifeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','point']


class ProductionsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(WifeInfo,WifeInfoAdmin)
admin.site.register(ProductionInfo,ProductionsInfoAdmin)
# admin.sites.