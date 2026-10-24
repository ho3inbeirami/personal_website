from django.db import models

# Create your models here.


class SiteSettings(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()
    copyright = models.CharField(max_length=500)
    