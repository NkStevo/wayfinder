# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Match

def index(request):
    dummy_user_list = Match.objects.order_by('first_name')[:10]
    context = {'dummy_user_list': dummy_user_list}
    return render(request, 'wayfinder_app/index.html', context)

def matches(request):
    dummy_match_list = Match.objects.order_by('first_name')[:10]
    context = {'matches': dummy_match_list[1:], 'first_match': dummy_match_list[0]}
    return render(request, 'wayfinder_app/matches.html', context)
