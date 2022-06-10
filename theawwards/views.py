from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import *
from.models import *

# Create your views here.

def home(request):
   
    
    return render(request, 'index.html')
