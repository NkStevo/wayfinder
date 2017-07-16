from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the first name of user"))
    last_name = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the last name"))
    address = models.CharField(max_length=300,blank=True,null=True,help_text=("enter the address"))
    phone_number = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the phone number"))
    email = models.EmailField(max_length=100,blank=True,null=True,help_text=("enter the email"))
    username = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the username"))
    creation_date = models.DateTimeField(editable=False,null=True)

    def save(self, *args, **kwargs):
        if not self.creation_date:
          self.creation_date = timezone.now()

        return super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.username
