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
