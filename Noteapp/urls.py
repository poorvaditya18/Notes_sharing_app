from django.contrib import admin
from django.urls import path
from .views import *

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
   path('edit_profile/',edit_profile,name="edit_profile")

]