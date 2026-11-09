from django.urls import path
from .views import *
urlpatterns = [
    path('',IndexPageView.as_view(), name= 'home'),
    path('about/',AboutPageView.as_view(), name ='about'),
    path('resume/',ResumeView.as_view(), name ='resume')
]
