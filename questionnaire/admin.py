from django.contrib import admin
from .models import Questionnaire
# Register your models here.

class QuestionnaireAdmin(admin.ModelAdmin):
	list_display= ['full_name', 'client_name', 'mobile']

admin.site.register(Questionnaire, QuestionnaireAdmin)
