from django.urls import path,include
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings


urlpatterns=[
    path('',views.home, name='home'),
    path('project/', views.new_project,name ='new_project'),
    path('search/',views.search_results,name='search_results'),
    path('profile/',views.profile,name='profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
