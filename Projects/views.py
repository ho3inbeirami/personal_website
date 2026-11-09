from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from . import models

class ProjectListView(ListView):
    template_name = 'Projects/project_list.html'
    model = models.Projects
    context_object_name = 'projects'