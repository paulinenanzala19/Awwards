from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib import messages
from .forms import *
from.models import *

# Create your views here.

def home(request):
    projects = Post.get_projects()
    context={
        'projects' : projects,
    }
   
    
    return render(request,'index.html', context)

def new_project(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if  prof_form.is_valid() and user_form.is_valid:
            user_form.save()
            prof_form.save()
            messages.success(request,f'Your account has been updated successfully!')

            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'user_form': user_form,           
        'prof_form': prof_form
    }

    return render(request, 'profile.html', context)

def update_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'prof_form': profile_form

        }

    return render(request, 'update_profile.html', context)

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": searched_posts})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})