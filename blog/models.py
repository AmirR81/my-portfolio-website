from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    technology = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    website_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:project_detail', args=(self.pk,))




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomment')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projectcomment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replycomment', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'
