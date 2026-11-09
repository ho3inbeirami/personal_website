from django.shortcuts import render

from django.views.generic import TemplateView
from SiteSettings.models import SiteSettings

class IndexPageView(TemplateView):
    template_name = 'MyWebPage/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = SiteSettings.objects.first()
        return context
    



class AboutPageView(TemplateView):
    template_name = 'MyWebPage/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = SiteSettings.objects.first()
        return context


class ResumeView(TemplateView):
    template_name = 'MyWebPage/resume.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site"] = SiteSettings.objects.first()
        return context


def headerComponent(request):
    context = {
        "site": SiteSettings.objects.first()
    }
    return render(request, 'header.html', context)


def footerComponent(request):
    context = {
        "site": SiteSettings.objects.first()
    }
    return render(request, 'footer.html', context)