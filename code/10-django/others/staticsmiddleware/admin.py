from django.contrib import admin

# Register your models here.

from .models import PicClass

class PicClassAdmin(admin.ModelAdmin):
    list_display = ['id','picture','idd']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['id']
    search_fields = ['id']

admin.site.register(PicClass,PicClassAdmin)