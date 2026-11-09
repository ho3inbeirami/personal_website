from django.urls import path
from .views import ContactUsPageView
urlpatterns = [
    path('contactus/',ContactUsPageView.as_view(), name='ContactUs')
]
