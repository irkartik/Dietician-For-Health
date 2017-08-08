from django.db import models
from datetime import datetime
# Create your models here.

class Catagory(models.Model):
	catagory_name = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Catagory"
		verbose_name_plural = "Catagories"

	def __str__(self):
		return self.catagory_name

class Package(models.Model):
	catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
	package_name = models.CharField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	p1 = models.IntegerField(verbose_name="Price for 2 months")
	p2 = models.IntegerField(verbose_name="Price for 3 months")
	p3 = models.IntegerField(verbose_name="Price for 6 months")
	p4 = models.IntegerField(verbose_name="Price for 12 months")
	p5 = models.IntegerField(verbose_name="Price for 18 months")
	offer_p1 = models.IntegerField(verbose_name="Offer Price for 2 months")
	offer_p2 = models.IntegerField(verbose_name="Offer Price for 3 months")
	offer_p3 = models.IntegerField(verbose_name="Offer Price for 6 months")
	offer_p4 = models.IntegerField(verbose_name="Offer Price for 12 months")
	offer_p5 = models.IntegerField(verbose_name="Offer Price for 18 months")

	class Meta:
		verbose_name = "Package"
		verbose_name_plural = "Packages"

	def __str__(self):
		return self.package_name
