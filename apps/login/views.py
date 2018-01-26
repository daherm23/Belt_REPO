from django.shortcuts import render
import re
from .models import User
import bcrypt
from django.contrib import messages
from django.contrib.messages import error
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'login/index.html')

def register(request):
    print 'welcome to my app'
    if request.method == 'POST':
        new_user = User.objects.val_Reg( #regval 
            request.POST['name'],
            request.POST['username'], 
            request.POST['email'],
            request.POST['password'],
            request.POST['pw_confirm']
            )
        if type(new_user) is list:
            for error in new_user:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
        else:
            request.session['user_id'] = new_user.id
            return redirect("/travels") 

def login(request):
    print 'welcome back person'
    
    if request.method == 'POST':
        login = User.objects.val_Log( #logval
            request.POST['email'],
            request.POST['password']
            )
        if type(login) is unicode:
            messages.add_message(request, messages.ERROR, login)
            return redirect('/')
        else:
            request.session['user_id'] = login.id
            return redirect("/travels") 


def logout(request):
    print 'goodbye'
    request.session.clear()	
    return redirect('/')
