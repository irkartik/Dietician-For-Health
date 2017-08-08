from django.db import models
from core.models import Client
# Create your models here.

gender_choice = (
	('M', 'Male'),
	('F', 'Female'),
	)
blood_choices = (
	('A+', 'A positive'),
	('A-', 'A negative'),
	('B+', 'B positive'),
	('B-', 'B negative'),
	('AB+', 'AB positive'),
	('AB-', 'AB negative'),
	('O+', 'O positive'),
	('O-', 'O negative'),
	)
yes_no_choice = (
	('Y', 'Yes'),
	('N', 'No'),
	)

class Questionnaire(models.Model):
	client_name = models.OneToOneField('core.Client', verbose_name="Client Username")
	full_name = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(max_length=1, choices=gender_choice)
	dob = models.DateField(verbose_name='Date of Birth')
	address = models.CharField(max_length=1000, verbose_name='Address')
	state = models.CharField(max_length=100, verbose_name='State/Province')
	mobile = models.IntegerField(verbose_name='Mobile Number')
	alternate_mobile = models.IntegerField(verbose_name='Alternate Mobile Number')
	email_id = models.EmailField(verbose_name='Email')
	goals = models.CharField(max_length=1000, verbose_name='Personal/Family Goals')

	height = models.IntegerField(verbose_name='Height (cms)')	
	weight = models.IntegerField(verbose_name='Weight (kg)')
	blood = models.CharField(max_length=3, choices=blood_choices, verbose_name='Blood Group')
	pressure = models.CharField(max_length=10,verbose_name='Blood Pressure (value1/value2) E.g. 120/80')
	bmi = models.CharField(max_length=100, verbose_name='Body Mass Index (Leave Blank if unknown)', null = True, blank = True)
	illness = models.CharField(max_length=1000, verbose_name='Provide details of Medical Illness/Condition (if any)', null = True, blank = True)
	surgery = models.CharField(max_length=1000, verbose_name='Your Surgery Details, if any', null = True, blank = True)
	illness_family = models.CharField(max_length=1000, verbose_name='Details of any illness of family (if any)', null = True, blank = True)

	reg_back = models.CharField(max_length=1000, verbose_name='Location details in country',blank=True, null=True)
	cul_back = models.CharField(max_length=1000, verbose_name='Provide details of Cultural Background',blank=True, null=True)
	diet_pref = models.CharField(max_length=1000, verbose_name='Diet Preference',blank=True, null=True)
	alcohol = models.CharField(max_length=1000, verbose_name='How frequently do you consume alcohol',blank=True, null=True)
	smoke = models.CharField(max_length=1000, verbose_name='How frequently do you smoke',blank=True, null=True)
	tobacco = models.CharField(max_length=1000, verbose_name='How frequently do you consume tobacco based mouth freshners',blank=True, null=True)
	fav_food = models.CharField(max_length=1000, verbose_name='Favorite Foods',blank=True, null=True)
	fav_fruit = models.CharField(max_length=1000, verbose_name='Favorite Fruits',blank=True, null=True)
	dislike_food = models.CharField(max_length=1000, verbose_name='Foods Disliked',blank=True, null=True)
	allergic_food = models.CharField(max_length=1000, verbose_name='Allergic Foods', blank=True, null=True)
	supplements = models.CharField(max_length=1000, verbose_name='Supplement Details (if any)', null = True, blank = True)
	food_consumed = models.CharField(max_length=1000, verbose_name='Please provide details of food type consumed',blank=True, null=True)
	home_cooked = models.CharField(max_length=1000, verbose_name='What percent fo your food is home cooked (rate from 0 to 1)',blank=True, null=True)
	out_cooked = models.CharField(max_length=1000, verbose_name='How often you eat outside food in a week?',blank=True, null=True)
	cupboard = models.CharField(max_length=1000, verbose_name="What foods would I always find in your refrigiator?",blank=True, null=True)
	nutritional_panels = models.CharField(max_length=1, verbose_name="Do you need nutritional panels?", choices=yes_no_choice, default='Y')

	wake_time = models.CharField(max_length=10, verbose_name="Wake Up",blank=True, null=True)
	sleed = models.CharField(max_length=10, verbose_name='Sleep',blank=True, null=True)
	training_morning = models.CharField(max_length=10, verbose_name='Morning Training Timing',blank=True, null=True)
	training_evening = models.CharField(max_length=10, verbose_name='Evening Training Timing',blank=True, null=True)
	school_timings = models.CharField(max_length=10, verbose_name="School Timings",blank=True, null=True)
	off_days = models.CharField(max_length=100, verbose_name='Off Days',blank=True, null=True)

	on_waking = models.CharField(max_length=100, verbose_name='On waking up (eg. A glass of milk)',blank=True, null=True)
	breakfast = models.CharField(max_length=100, verbose_name='Breakfast (First meal of the day)',blank=True, null=True)
	brunch = models.CharField(max_length=100,blank=True, null=True)
	lunch = models.CharField(max_length=100,blank=True, null=True)
	evening_snacks = models.CharField(max_length=100, verbose_name='Evening High Tea and Snacks',blank=True, null=True)
	supper = models.CharField(max_length=100,blank=True, null=True)
	dinner = models.CharField(max_length=100,blank=True, null=True)

	additional_comments = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.full_name