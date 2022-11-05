from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('index/',index,name="index"), # home page
   path('about/',about,name="about"),
   path('contact/',contact,name='contact'),
   path('login/',userlogin,name='userlogin'),
   path('signup/',usersignup,name='signup'),
   path('login_admin/',login_admin,name='login_admin'),
   path('admin_home/',admin_home,name="admin_home"),
   path('logout/',Logout,name='Logout'),
   path('profile/',profile,name='profile'),
   path('change_password/',changepwd,name="changepwd"),
   path('edit_profile/',edit_profile,name="edit_profile"),
   path('upload_notes/',upload_notes,name="upload_notes"),
   path('view_mynotes',view_mynotes,name='view_mynotes'),
   path('delete_mynotes/<int:pid>',view_mynotes,name='delete_mynotes')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)