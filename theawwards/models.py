from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = Post.objects.all()
        return projects

    @classmethod
    def search_project(cls,search_term):
        project = Post.objects.filter(title__icontains=search_term)
        return project


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=100)
    contact=models.IntegerField(default=0)
    location = models.CharField(max_length=60, blank=True)

    def save_profile(self):
        super().save()


