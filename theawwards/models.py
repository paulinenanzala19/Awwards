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


class Ratings(models.Model):
    ratings=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10',)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)
    design_rate = models.IntegerField(choices=ratings, default=0, blank=True)
    usability_rate = models.IntegerField(choices=ratings, blank=True, default=0)
    content_rate = models.IntegerField(choices=ratings, blank=True,default=0)
    overall_score = models.FloatField(default=0, blank=True)

    def save_ratings(self):
        self.save()

    def __str__(self):
        return f'{self.post} Ratings'

    @classmethod
    def get_ratings(cls, id):
        ratings = Ratings.objects.filter(post_id=id).all()
        return ratings
