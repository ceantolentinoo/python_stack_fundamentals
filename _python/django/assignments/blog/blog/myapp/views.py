from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')
def index(request):
    return render(request, "index.html")
def new(request):
    return HttpResponse("CREATE new blog page")
def create(request):
    return redirect('/')
def show(request, id):
    return HttpResponse(f"SHOWING blog number {id}")
def edit(request, id):
    return HttpResponse(f"EDITING blog number {id}")
def destroy(request, id):
    return HttpResponse(f"DELETING blog number {id}")
def blogsJson(request):
    return JsonResponse({"title": "", "content": ""})
def some_function(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return redirect("/")

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form
    }
    return render(request,"show.html",context)

# Create your views here.
