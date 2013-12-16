from django.template import loader, Template, Context
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login


import datetime

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def login_user(request):
    template = loader.get_template('auth.html')
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username})

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