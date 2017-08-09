from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (
        ('AM', 'Admin'),
        ('CM', 'Client'),
        ('PM', 'Panel'),
        ('DM', 'Dietician'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='CM')

class Dietician(models.Model):
    user_name = models.OneToOneField('CustomUser', verbose_name="Name")
    qualification = models.CharField(max_length=1000)
    address = models.CharField(null=True, max_length=10000)

    class Meta:
        verbose_name = "Dietician"

    def __str__(self):
        return self.user_name.username

class Client(models.Model):
    user_name = models.OneToOneField('CustomUser')
    dietician = models.ForeignKey(Dietician)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000,blank=True, null=True)
    about_me = models.TextField(max_length=10000,blank=True, null=True)

    class Meta:
        verbose_name = 'Client'

    def __str__(self):
        return self.user_name.username

class Panel(models.Model):
    type_choices = (
        ('DO', 'Doctor'),
        ('NE', 'Neuropath'),
    )
    user_name = models.OneToOneField('CustomUser', verbose_name="Name")
    panel_type = models.CharField(max_length=2, choices=type_choices, default='DO')
    qualification = models.CharField(max_length=1000)
    address = models.CharField(null=True, max_length=10000)

    class Meta:
        verbose_name = "Panel"

    def __str__(self):
        return self.user_name.username

class Testimonial(models.Model):
    testiment_name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.testiment_name

class Video(models.Model):
    video_name = models.CharField(max_length=1000)
    url = models.CharField(max_length=10000000)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video"

    def __str__(self):
        return self.video_name

class TopAdBar(models.Model):
    ad_text = models.CharField(max_length=1000)
    url = models.CharField(max_length=10000)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name="Ad Bar Section"
        verbose_name_plural= "Ad Bar Section"

    def __str__(self):
        return self.ad_text

class SocialNetwork(models.Model):
    social_platform = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    order = models.PositiveIntegerField()
    img = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = "Social Networks"

    def __str__(self):
        return self.social_platform


class Banner(models.Model):
    banner_name = models.CharField(max_length = 1000)

    banner_class = models.CharField(max_length=100, blank=True, null = True)

    package1_id = models.CharField(max_length=100, verbose_name="Technical stuff (to be used by developers", null = True, blank=True)
    package1_name = models.CharField(max_length=1000)
    package1_url = models.CharField(max_length=10000, blank=True, null=True)
    package1_img = models.FileField()

    package2_id = models.CharField(max_length=100, verbose_name="Technical stuff (to be used by developers", null = True, blank=True)
    package2_name = models.CharField(max_length=1000)
    package2_url = models.CharField(max_length=10000, blank=True, null=True)
    package2_img = models.FileField()

    package3_id = models.CharField(max_length=100, verbose_name="Technical stuff (to be used by developers", null = True, blank=True)
    package3_name = models.CharField(max_length=1000)
    package3_url = models.CharField(max_length=10000, blank=True, null=True)    
    package3_img = models.FileField()

    package4_id = models.CharField(max_length=100, verbose_name="Technical stuff (to be used by developers", null = True, blank=True)
    package4_name = models.CharField(max_length=1000)
    package4_url = models.CharField(max_length=10000, blank=True, null=True)    
    package4_img = models.FileField()

    banner_tagline = models.CharField(max_length=1000)

    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Banner Package"
        verbose_name_plural = "Banner Packages"

    def __str__(self):
        return self.banner_name
