from django.contrib import admin
from .models import Notification
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
	list_display = ['title', 'notification_for']
	list_filter = ['notification_for']
	search_fields = ['title']

admin.site.register(Notification, NotificationAdmin)