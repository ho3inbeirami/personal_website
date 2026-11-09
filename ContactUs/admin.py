from django.contrib import admin

# Register your models here.
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display= ['full_name', 'email','phone_number','message','date']
    

admin.site.register(ContactUs,ContactUsAdmin)