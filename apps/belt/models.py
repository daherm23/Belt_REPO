from __future__ import unicode_literals

from ..login.models import User

from django.db import models

import datetime

class TripManager(models.Manager):
    def addTrip(self, post_data):
       
        errors = []
        present = datetime.datetime.now()

        if len(post_data['destination']) < 1: 
            errors.append('Destination field cannot be empty!')
        if len(post_data['start_date']) < 1:
            errors.append('Travel Date From field cannot be empty!')
        elif post_data['start_date'] < str(present):
            errors.append('Error! Start date cannot be scheduled before present day!')
        if len(post_data['end_date']) < 1:
            errors.append('Travel Date To field cannot be empty!')
        elif post_data['start_date'] > post_data['end_date']:
            errors.append('Error! Travel Date From field cannot be after Travel Date To field! Choose a different date!')
        if len(post_data['desc']) < 1:
            errors.append('Error! Description field is empty!')
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=350)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name ='trips')
    companion = models.ManyToManyField(User, related_name ='buddy_pass')
    objects = TripManager()
