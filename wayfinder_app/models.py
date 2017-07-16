from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the first name of user"))
    last_name = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the last name"))
    occupation = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the occupation name"))
    age = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the age"))
    city = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the city name"))
    state = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the state name"))
    address = models.CharField(max_length=300,blank=True,null=True,help_text=("Enter the address"))
    phone_number = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the phone number"))
    email = models.EmailField(max_length=100,blank=True,null=True,help_text=("Enter the email"))
    username = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the username"))
    college = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the college"))
    employer = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the employer"))
    linkedin_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the linkedin link"))
    facebook_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the facebook link"))
    avatar_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the avatar link"))
    creation_date = models.DateTimeField(editable=False,null=True)

class Match(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the first name of user"))
    last_name = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the last name"))
    occupation = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the occupation name"))
    age = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the age"))
    city = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the city name"))
    state = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the state name"))
    college = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the college"))
    employer = models.CharField(max_length=100,blank=True,null=True,help_text=("Enter the employer"))
    linkedin_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the linkedin link"))
    facebook_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the facebook link"))
    avatar_link = models.CharField(max_length=2083,blank=True,null=True,help_text=("Enter the avatar link"))



    def save(self, *args, **kwargs):
        if not self.creation_date:
          self.creation_date = timezone.now()

        return super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.username
