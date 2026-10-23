from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ContactUsPageView(TemplateView):
    template_name = 'ContactUs/ContactUs.html'


