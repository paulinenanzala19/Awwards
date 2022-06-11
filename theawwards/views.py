from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import *
from.models import *

# Create your views here.

def home(request):
    projects = Post.get_projects()
    context={
        'projects' : projects,
    }
   
    
    return render(request,'index.html', context)

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  prof_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('profile')

    else:
        
        prof_form = ProfileUpdateForm(instance=request.user)
        

        context = {
           
            'prof_form': prof_form
        }

        return render(request, 'profile.html', context)
