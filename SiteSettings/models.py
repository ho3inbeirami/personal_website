from django.db import models

# Create your models here.


class SiteSettings(models.Model):
    title = models.CharField(max_length=100,default="", verbose_name ='Title')
    site_url = models.URLField(max_length=100,null=True, blank=True, verbose_name ='Site url')
    copyright = models.TextField(verbose_name ='Copy Right')
    address = models.TextField(default="", verbose_name ='Address')
    telephone = models.CharField(max_length=11,null=True, blank=True, verbose_name ='Telephone')
    email= models.EmailField(max_length=200,null=True, blank=True, verbose_name ='Email')
    about = models.TextField(verbose_name ='About me')
    resume = models.FileField(upload_to='resume',blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'settings'
        verbose_name = 'setting'
        verbose_name_plural = 'settings'