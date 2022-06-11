from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('image', 'title', 'url', 'description', 'technologies',)

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image','bio']
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
     

    class Meta:
        model = User
        fields = ['username','email']