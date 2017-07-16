# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    dummy_user_list = User.objects.order_by('creation_date')[:10]
    context = {'dummy_user_list': dummy_user_list}
    return render(request, 'wayfinder_app/index.html', context)

def matches(request):
    dummy_user_list = User.objects.order_by('creation_date')[:10]
    context = {'matches': dummy_user_list[1:], 'first_match': dummy_user_list[0]}
    return render(request, 'wayfinder_app/matches.html', context)
