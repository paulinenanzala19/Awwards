from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='pepe')
        self.post = Post.objects.create(id=1, title='picture_patch', image='flower5.png', description='testing',user=self.user, url='https:nanzalapatch.heroku.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_by_title('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_by_title('test')
        self.assertTrue(len(post) < 1)

class ProfileTest(TestCase):
    def setUp(self):
        self.pepe = User(username = 'Pepe',email = 'test@gmail.com')
        self.pepe = Profile(user = self.pepe,id = 1,bio = 'koding and kahawa',image = 'image.jpg',date='Jun,6,2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.pepe,Profile))


    def test_delete_user(self):
        self.pepe.delete_user()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles),0)