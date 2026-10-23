from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'MyWebPage/index.html'



class AboutPageView(TemplateView):
    template_name = 'MyWebPage/about.html'

