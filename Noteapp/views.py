import email
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest , request, response
from datetime import date
# Create your views here.

# homepage 
def index(request):
    return render(request,'index.html')

# about ->
def about(request):
    return render(request,'about.html')

# contact 
def contact(request):
    return render(request,'contact.html')


# ------------------------------------------------------


#  user_login
def userlogin(request):
    error = True
    if request.method == 'POST':
        emailid = request.POST['emailid']
        pwd = request.POST['pwd']
        #authenticate with the admin users
        user = authenticate(username=emailid,password=pwd)
        try:
            if user:
                login(request,user)
                error = False
            else:
                error = True
        except:
            error=True
    context ={'error':error}               
    return render(request,'login.html',context) 

# usersignup 
def usersignup(request):
    error=True
    if request.method == "POST":
        first_name= request.POST['fname']
        last_name = request.POST['lname']
        contact = request.POST['contact']
        emailid = request.POST['emailid']
        password = request.POST['pwd']
        branch = request.POST['branch']
        role = request.POST['role']
        try:
            user = User.objects.create_user(username=emailid,first_name=first_name,last_name=last_name,password=password)
            Signup.objects.create(user=user,contact=contact,branch=branch,role=role)
            error=False
        except:
            error=True
    context ={'error':error}          
    return render(request,'signup.html',context)


# userprofile
def profile(request):
    if not request.user.is_authenticated:
        # if user is not authenticated then redirect to login page
        return redirect('login')

    # as user is stored both in user and signupuser
    user = User.objects.get(id=request.user.id)
    signup_user = Signup.objects.get(user=user)
    context = {'data':signup_user,'user':user}    
    return render(request,'profile.html',context)    



# change password 
def changepwd(request):
    error=True
    if not request.user.is_authenticated:
        # if user is not authenticated then redirect to login page
        return redirect('userlogin')
    if request.method == 'POST':
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd'] 
        cnfpwd = request.POST['cnfpwd']
        if cnfpwd == newpwd:
            user = User.objects.get(username__exact=request.user.username)
            user.set_password(newpwd)
            user.save()
            error=False
        else:
            error=True
    context={'error':error}            
    return render(request,'changepwd.html',context)



def edit_profile(request):
    if not request.user.is_authenticated:
        # if user is not authenticated then redirect to login page
        return redirect('login')
    # as user is stored both in user and signupuser
    user = User.objects.get(id=request.user.id)
    signup_user = Signup.objects.get(user=user)
    flag=False
    if request.method =="POST":
        fname= request.POST['fname']
        lname=request.POST['lname']
        # emailid = request.POST['emailid']
        contact = request.POST['contact']
        branch=request.POST['branch']
        user.first_name = fname
        user.last_name = lname
        signup_user.contact = contact
        signup_user.branch = branch
        user.save()
        signup_user.save()
        flag= True
    context = {'data':signup_user,'user':user,'flag':flag}    
    return render(request,'edit_profile.html',context)  


def upload_notes(request):
    if not request.user.is_authenticated:
        # if user is not authenticated then redirect to login page
        return redirect('login')
    error=True
    if request.method == "POST":
        branch= request.POST['branch']
        subject = request.POST['subject']
        notes = request.FILES['notesfile']
        filetype = request.POST['filetype']
        description = request.POST['description']
        user = User.objects.filter(username = request.user.username).first()
        try:
            Note.objects.create(user=user,uploadingdate=date.today(),branch=branch,subject=subject,notesfile=notes,filetype=filetype,description=description)
            error=False
        except:
            error=True
    context ={'error':error}          
    return render(request,'upload_notes.html',context)


def view_mynotes(request):
    if not request.user.is_authenticated:
        # if user is not authenticated then redirect to login page
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Note.objects.filter(user=user)
    context = {'notes':notes}    
    return render(request,'view_mynotes.html',context)  


def delete_mynotes(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Note.objects.get(id=id)
    notes.delete()
    return redirect('view_mynotes')    

    

#--------------------------------------------------------


# adminlogin
def login_admin(request):
    error = True
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        #authenticate with the admin users
        user = authenticate(username=uname,password=pwd)
        try:
            if user.is_staff:
                # so user can access the admin panel
                login(request,user)
                error = False
            else:
                error = True
        except:
            error=True
    context ={'error':error}               
    return render(request,'login_admin.html',context) 

# adminhome
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request,'admin_home.html')    

#adminlogout
def Logout(request):
    logout(request)
    return redirect('index')
