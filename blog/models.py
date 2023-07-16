from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    technology = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    website_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

