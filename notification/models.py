from django.db import models
from core.models import CustomUser
from datetime import datetime

# Create your models here.
class Notification(models.Model):
	notification_for = models.ForeignKey(CustomUser)
	title = models.CharField(max_length=1000)
	body = models.TextField(max_length=1000000)
	created_at = models.DateTimeField(auto_now_add=True)
	viewed = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Notification"

	def __str__(self):
		return self.title