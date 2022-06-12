from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from .forms import *
from.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .serializers import *
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Post.get_projects()
    context={
        'projects' : projects,
    }
   
    
    return render(request,'index.html', context)

@login_required(login_url='/accounts/login/')
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

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def project(request, post):
    post = Post.objects.get(title=post)
    ratings = Ratings.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Ratings.objects.filter(post=post)

            design_ratings = [des.design_rate for des in post_ratings]
            design_avr = sum(design_ratings) / len(design_ratings)

            usability_ratings = [usa.usability_rate for usa in post_ratings]
            usability_avr = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content_rate for content in post_ratings]
            content_avr = sum(content_ratings) / len(content_ratings)

            overall_score = (design_avr + usability_avr + content_avr) / 3
            print(overall_score)
            
            rate.design_avr = round(design_avr, 2)
            rate.usability_avr = round(usability_avr, 2)
            rate.content_avr = round(content_avr, 2)
            rate.overall_score = round(overall_score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'ratings.html', params)
