from django.contrib import admin

from django.contrib import admin
from .models import summer,monsoon


class summerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'expiry_date', 'manufacturing_date')
    search_fields = ('name',)
    list_filter = ('expiry_date', 'manufacturing_date')
admin.site.register(summer,summerAdmin)
 
                  
class monsoonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'expiry_date', 'manufacturing_date')
    search_fields = ('name',)
    list_filter = ('expiry_date', 'manufacturing_date')
admin.site.register(monsoon,monsoonAdmin)