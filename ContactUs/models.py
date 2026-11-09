from django.db import models

from django.core.validators import MaxLengthValidator,MinLengthValidator
# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200,blank=False,null=False)
    phone_number = models.IntegerField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])
    email =  models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    def __str__(self):
        return f'from {self.full_name}, mobile: {self.phone_number}'