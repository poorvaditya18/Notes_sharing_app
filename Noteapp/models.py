from distutils.command.upload import upload
from enum import auto
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

# signup -> user's details will be stored here
class Signup(models.Model):
    # so if user get's deleted the from signup user will also get deleted.
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    branch = models.CharField(max_length =30)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    

class Note(models.Model):
    # so if user get's deleted  user's notes  will also get deleted.
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

    uploadingdate = models.DateField(auto_now_add=True)
    
    branch = models.CharField(max_length =30)
    
    subject = models.CharField(max_length=30,null=True)

    notesfile = models.FileField(null=True)

    filetype = models.CharField(max_length=30,null=True)
    
    description = models.CharField(max_length=200,null=True)
    
    status = models.CharField(max_length=15) 

    def __str__(self):
        return self.Signup.user.username + self.status
    