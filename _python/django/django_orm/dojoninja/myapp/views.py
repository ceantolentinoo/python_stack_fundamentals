from django.shortcuts import render,redirect
from .models import Ninja, Dojo

def index(request):
    all_dojos = Dojo.objects.all()
    context = {"dojos": all_dojos}
    return render(request, "index.html", context)

def create_ninja(request):
    data = request.POST
    dojo = Dojo.objects.get(id=data['dojo'])
    new_ninja = Ninja.objects.create(first_name=data['fname'], last_name=data['lname'], dojo=dojo)
    print(Ninja.objects.all())
    return redirect("/")

def create_dojo(request):
    data = request.POST
    new_dojo = Dojo.objects.create(name=data['name'], city=data['city'], state=data['state'])
    print(Dojo.objects.all())
    return redirect("/")
    
# Create your views here.
