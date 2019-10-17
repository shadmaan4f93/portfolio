from django.db import models
from django_mysql.models import ListCharField

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    logo = models.ImageField(upload_to='logo/')
    weblink = models.URLField(blank=True)
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    logo = models.ImageField(upload_to='logo/') 
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name

class HomePage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    cv = models.FileField(upload_to='documents/')
    specialize = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    skils = ListCharField(
        base_field=models.CharField(max_length=10),
        size=10,
        max_length=(10 * 12)
    )
    address = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)
    google_profile = models.URLField(blank=True)

    def __str__(self):
        return self.title
