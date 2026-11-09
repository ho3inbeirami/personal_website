from django.shortcuts import render
from django.views import View
# Create your views here.
from .forms import ContactUsForm

from django.http import HttpRequest,HttpResponse
from .models import ContactUs
class ContactUsPageView(View):
    def get(self,request: HttpRequest):
        form = ContactUsForm()
        context = {'form':form}
        return render(request,'ContactUs/ContactUs.html',context)
    
    def post(self,request: HttpRequest):
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            phone_number = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            data = ContactUs(full_name=full_name,phone_number= phone_number,email= email,message= message)
            data.save()
            context = {'form':ContactUsForm(),'Success':'message was sent' }
            return render(request,'ContactUs/ContactUs.html',)
        context = {'form':form, 'failure':'please check form'}
        return render(request,'ContactUs/ContactUs.html',context)



