from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from questionnaire.models import Questionnaire

class QuestionnaireForm(forms.ModelForm):

	class Meta:
		model = Questionnaire
		fields = ['full_name','gender','dob','address','state','mobile','alternate_mobile',
		'email_id','goals','height','weight','blood','pressure','bmi','illness','surgery','illness_family',
		'reg_back','cul_back','diet_pref','alcohol','smoke','tobacco','fav_food','fav_fruit','dislike_food',
		'allergic_food','supplements','food_consumed','home_cooked','out_cooked','cupboard','nutritional_panels',
		'wake_time','sleed','training_morning','training_evening','school_timings','off_days','on_waking','breakfast',
		'brunch','lunch','evening_snacks','supper','dinner','additional_comments']
		exclude = ['client_name']


