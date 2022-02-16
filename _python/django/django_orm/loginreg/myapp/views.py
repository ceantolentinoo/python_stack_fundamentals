from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def user_reg(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, extra_tags=key)
        return redirect('/register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(first_name = request.POST['fname'],
        last_name = request.POST['lname'], email = request.POST['email'],
        username = request.POST['username'], password=pw_hash)
        messages.add_message(request, messages.INFO,"User created!", extra_tags="userCreated")
        return redirect('/')

def user_login(request):
    user = User.objects.filter(email = request.POST['email'])
    if len(user) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
            return redirect('/success')
        else:
            messages.add_message(request, messages.ERROR,"Invalid email/password!", extra_tags="loginError")
            return redirect('/')
    else:
        messages.add_message(request, messages.ERROR,"Invalid email/password!", extra_tags="loginError")
        return redirect('/')

def success(request):
    return render(request, "success.html")

# Create your views here.
