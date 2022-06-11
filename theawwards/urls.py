from django.urls import path,include
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings


urlpatterns=[
    path('',views.home, name='home'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
