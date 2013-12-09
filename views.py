from django.template import loader, Template, Context
from django.http import HttpResponse
from django.shortcuts import render

import datetime

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def profile(request):
    template = loader.get_template('profile.html')
    return render(request, 'profile.html')

def services(request):
    template = loader.get_template('services.html')
    return render(request, 'services.html')

def contact(request):
    template = loader.get_template('contact.html')
    return render(request, 'contact.html')

def about(request):
    template = loader.get_template('about.html')
    return render(request, 'about.html')