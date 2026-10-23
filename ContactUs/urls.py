from django.urls import path
from .views import ContactUsPageView
urlpatterns = [
    path('contact-us',ContactUsPageView.as_view())
]
