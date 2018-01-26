from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login import *
from .models import *
from django.contrib import messages

def index(request):
	print 'you made it home'
	context = {
	'user': User.objects.get(id=request.session['user_id']),
	'destinations': Trip.objects.filter(uploader=request.session['user_id'])| Trip.objects.filter(companion=request.session['user_id']), 
	'trips': Trip.objects.exclude(uploader=request.session['user_id']).exclude(companion=request.session['user_id'])
	}
	return render(request, "belt/index.html", context)

def destination(request, id):
	print 'destination'
	context = {
    'trip': Trip.objects.get(id=id),
    'user': User.objects.get(id=request.session['user_id']),
    'homies': User.objects.filter(buddy_pass=id),
    }
	return render(request, 'belt/destination.html', context)

def add_travel(request):
	print 'Vacation time' 

	return render(request, "belt/add.html")

def create(request):
	print 'Youre booked'
	errors = Trip.objects.addTrip(request.POST) 
	if errors: 
		for error in errors:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/travels/add")
	else: 
		Trip.objects.create(destination=request.POST['destination'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], desc=request.POST['desc'], uploader=User.objects.get(id=request.session['user_id'])) 
	return redirect("/travels")

def join(request, id):
	this_user= User.objects.get(id=request.session['user_id'])
	this_vacay = Trip.objects.get(id=id)
	this_vacay.companion.add(this_user)
	return redirect('/travels')





