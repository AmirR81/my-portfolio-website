from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'website_url')
    abstract = False

admin.site.register([Project], ProjectAdmin)
