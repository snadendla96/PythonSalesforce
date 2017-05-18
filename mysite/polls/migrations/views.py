# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.https import HttpResponse


#the index will refere to the page name
def index(request):
   return HttpResponse("Hello, World.you are at the polls index page")
   