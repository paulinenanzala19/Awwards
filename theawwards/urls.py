from django.urls import path,include
from . import views
from django.urls import path,include
from .views import *
from django.conf import settings


urlpatterns=[
    path('',views.home, name='home'),
    
]
