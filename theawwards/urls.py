from django.urls import path,include
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)
router.register('users', views.UserViewSet)


urlpatterns=[
    path('',views.home, name='home'),
    path('project/', views.new_project,name ='new_project'),
    path('search/',views.search_results,name='search_results'),
    path('profile/',views.profile,name='profile'),
    path('ratings/<post>/', views.project, name='ratings'),
    path('api/', include(router.urls)),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
