from django.contrib import admin
from .models import *

# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
	list_display = ['catagory_name' , 'updated_at']
	search_fields = ['catagory_name']

class PackageAdmin(admin.ModelAdmin):
	list_display = ['package_name', 'catagory', 'updated_at']
	list_filter = ['catagory']
	search_fields = ['package_name']

admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Package, PackageAdmin)