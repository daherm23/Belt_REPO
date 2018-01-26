from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')



class UserManager(models.Manager): 
   def val_Reg(self, name, username, email, password, pw_confirm):
        errors = []
        if len(name) < 3:
            errors.append("Name must be more than 3 characters!")
        else:   
            for char in name:
                if str(char).isdigit():
                    errors.append("Name field can only contain letters") 
        if len(username) < 3:
            errors.append("Username must be more than 3 characters!")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long!")
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())         
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email address!")
        else:   
            emails = User.objects.filter(email=email)
            if len(emails) != 0:    
                errors.append("Email is invalid!")
        if password != pw_confirm:
            errors.append("Passwords do not match! Please try again!")
        if len(errors) > 0:
            return errors   
        else:
            new_user = User.objects.create(name=name, username=username, email=email, password=hashed)
            return new_user 
   def val_Log(self, email, password):
        user = User.objects.filter(email=email)
        print user
        if len(user) == 0:
            return "Invalid email!"
        elif bcrypt.checkpw(password.encode(), user[0].password.encode()) == False:
            return "Incorrect password!"
        else:   
            return user[0] 

class User(models.Model):
    name = models.CharField(max_length=100)
    username= models.CharField(max_length =100, default=1)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()