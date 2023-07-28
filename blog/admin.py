from django.contrib import admin
from .models import Project, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'website_url')
    list_filter = ('created_at',)
    search_fields = ('title', 'body')

admin.site.register([Project], ProjectAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'created_at', 'is_reply')
    raw_id_fields = ('user', 'project', 'reply')