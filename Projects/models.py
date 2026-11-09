from django.db import models

# Create your models here.

class ProjectImages(models.Model):
    image = models.ImageField(upload_to='images/projects', verbose_name='Image', null=True, blank=True)
    



class Projects(models.Model):
    title = models.CharField(max_length=400, verbose_name='Title')
    requirement = models.CharField(max_length=600, verbose_name='Requirement')
    description = models.TextField(verbose_name='Description')
    images = models.ManyToManyField("ProjectImages", verbose_name="Images")
    github = models.URLField(verbose_name='GitHub')
    is_active = models.BooleanField(default=True, verbose_name='active /de-active')
    
    
    
    
