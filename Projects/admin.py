from django.contrib import admin

# Register your models here.

from .models import Projects, ProjectImages
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title','github','is_active']
    


admin.site.register(Projects, ProjectsAdmin)

admin.site.register(ProjectImages)