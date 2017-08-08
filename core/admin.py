from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['username','first_name','last_name', 'email','user_type']
    list_filter = ('user_type',)
    search_fields = ['username','email','user_type']
    # list_editable = ['user_type']	

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email','username', 'user_type', 'password1',
                       'password2')}
         ),
    )

class DieticianAdmin(admin.ModelAdmin):
	list_display= ['user_name', 'qualification', 'address']
	search_fields = ['user_name']

class PanelAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'panel_type', 'qualification']
	list_filter = ['panel_type']
	search_fields = ['user_name']

class ClientAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'dietician', 'address']
	list_filter = ['dietician']
	search_fields = ['user_name']

class TestimonialAdmin(admin.ModelAdmin):
    list_display= ['testiment_name']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class VideoAdmin(admin.ModelAdmin):
    list_display= ['video_name', 'url']
    list_editable = ['url']

    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class TopAdBarAdmin(admin.ModelAdmin):
    list_display= ['order', 'ad_text', 'url']
    readonly_fields=('order',)
    list_editable = ['ad_text']

    actions = None 

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class SocialNetworkAdmin(admin.ModelAdmin):
    list_display= ['order', 'social_platform', 'url']
    readonly_fields=('order',)
    list_editable = ['url']
    ordering = ('order',)

    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Dietician, DieticianAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Panel, PanelAdmin)

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(TopAdBar, TopAdBarAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)

admin.site.unregister(Group)
